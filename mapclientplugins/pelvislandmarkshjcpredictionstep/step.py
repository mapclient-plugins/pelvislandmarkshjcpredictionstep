'''
MAP Client Plugin Step
'''

import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.pelvislandmarkshjcpredictionstep.configuredialog import ConfigureDialog
from mapclientplugins.pelvislandmarkshjcpredictionstep.hjcpredictionviewerwidget import MayaviHJCPredictionViewerWidget

from gias2.musculoskeletal import pelvis_hjc_estimation as hjc
from gias2.musculoskeletal import model_alignment as ma
import numpy as np

METHODS = ('Seidel', 'Bell', 'Tylkowski')
POP_CLASS = ('adults', 'men', 'women')
HIPLANDMARKS = ('LASIS', 'RASIS', 'LPSIS', 'RPSIS', 'PS')


class PelvisLandmarksHJCPredictionStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(PelvisLandmarksHJCPredictionStep, self).__init__('Pelvis Landmark HJC Prediction', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Anthropometry'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'python#dict'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'python#dict'))
        self._config = {}
        self._config['identifier'] = ''
        self._config['Prediction Method'] = METHODS[0]
        self._config['Population Class'] = POP_CLASS[0]
        self._config['GUI'] = True
        for l in HIPLANDMARKS:
            self._config[l] = l

        self._landmarks = None
        self._hipLandmarks = None
        self._hipLandmarksAligned = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        self._landmarks['HJC_left'] = np.array([0, 0, 0], dtype=float)
        self._landmarks['HJC_right'] = np.array([0, 0, 0], dtype=float)
        self._getHipLandmarks()
        self._alignHipCS()

        self._hipLandmarks['HJC_left'] = np.array([0, 0, 0], dtype=float)
        self._hipLandmarks['HJC_right'] = np.array([0, 0, 0], dtype=float)
        self._hipLandmarksAligned['HJC_left'] = np.array([0, 0, 0], dtype=float)
        self._hipLandmarksAligned['HJC_right'] = np.array([0, 0, 0], dtype=float)

        if self._config['GUI']:
            print('launching prediction gui')
            self._widget = MayaviHJCPredictionViewerWidget(self._landmarks,
                                                           self._config,
                                                           self.predict,
                                                           METHODS,
                                                           POP_CLASS)
            self._widget._ui.acceptButton.clicked.connect(self._doneExecution)
            self._widget._ui.abortButton.clicked.connect(self._abort)
            self._widget.setModal(True)
            self._setCurrentWidget(self._widget)
        else:
            self.predict()
            self._doneExecution()

    def _abort(self):
        raise RuntimeError('HJC Prediction Aborted')

    def _getHipLandmarks(self):
        self._hipLandmarks = {}
        for l in HIPLANDMARKS:
            lname = self._config[l]
            try:
                self._hipLandmarks[l] = self._landmarks[lname]
            except KeyError:
                raise RuntimeError('HJC prediction failed, missing landmark: ' + lname)

    def _alignHipCS(self):
        # align landmarks to hip CS
        hipLandmarks = list(self._hipLandmarks.items())
        landmarkNames = [l[0] for l in hipLandmarks]
        landmarkCoords = np.array([l[1] for l in hipLandmarks])
        landmarkCoordsAligned, alignT = ma.alignAnatomicPelvis(landmarkCoords,
                                                               self._hipLandmarks['LASIS'],
                                                               self._hipLandmarks['RASIS'],
                                                               self._hipLandmarks['LPSIS'],
                                                               self._hipLandmarks['RPSIS'],
                                                               returnT=True)
        self._hipLandmarksAligned = dict(list(zip(landmarkNames, landmarkCoordsAligned)))
        self._inverseT = np.linalg.inv(np.vstack([alignT, [0, 0, 0, 1]]))

    def predict(self):
        # run predictions methods
        print('predicting using %s (%s)' % (self._config['Prediction Method'],
                                            self._config['Population Class'],
                                            ))
        if self._config['Prediction Method'] == 'Seidel':
            self._predict(('LASIS', 'RASIS', 'LPSIS', 'RPSIS', 'PS'), hjc.HJCSeidel)
        elif self._config['Prediction Method'] == 'Tylkowski':
            self._predict(('LASIS', 'RASIS'), hjc.HJCTylkowski)
        elif self._config['Prediction Method'] == 'Bell':
            self._predict(('LASIS', 'RASIS', 'PS'), hjc.HJCBell)

    def _predict(self, reqLandmarks, predictor):
        L = []
        for l in reqLandmarks:
            try:
                L.append(self._hipLandmarksAligned[l])
            except KeyError:
                raise RuntimeError('HJC prediction failed, missing landmark: ' + l)
        L.append(self._config['Population Class'])
        predictions = np.array(predictor(*L)[:2])

        self._hipLandmarksAligned['HJC_left'] = predictions[0]
        self._hipLandmarksAligned['HJC_right'] = predictions[1]

        self._hipLandmarks['HJC_left'], \
        self._hipLandmarks['HJC_right'] = ma.transform3D.transformAffine(predictions, self._inverseT)
        self._landmarks['HJC_left'], \
        self._landmarks['HJC_right'] = ma.transform3D.transformAffine(predictions, self._inverseT)

        # self._hipLandmarks['HJC_left'] = ma.transform3D.transformAffine( [predictions[0],], self._inverseT )
        # self._hipLandmarks['HJC_right'] = ma.transform3D.transformAffine( [predictions[1],], self._inverseT )
        # self._landmarks['HJC_left'] = ma.transform3D.transformAffine( [predictions[0],], self._inverseT )
        # self._landmarks['HJC_right'] = ma.transform3D.transformAffine( [predictions[1],], self._inverseT )

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        self._landmarks = dataIn  # ju#landmarks

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._landmarks  # ju#landmarks

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        # dlg = ConfigureDialog(METHODS, POP_CLASS)
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        '''
        self._config.update(json.loads(string))

        # d = ConfigureDialog(METHODS, POP_CLASS)
        d = ConfigureDialog(self._main_window)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
