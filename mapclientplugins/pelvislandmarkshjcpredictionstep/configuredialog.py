

from PySide import QtGui
from mapclientplugins.pelvislandmarkshjcpredictionstep.ui_configuredialog import Ui_Dialog

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''

class ConfigureDialog(QtGui.QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, methods, popClasses, parent=None):
        '''
        Constructor
        '''
        QtGui.QDialog.__init__(self, parent)
        
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None

        self._methods = methods
        self._popClasses = popClasses
        self._makeConnections()
        self._initOptions()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)

    def _initOptions(self):
        for m in self._methods:
            self._ui.comboBoxMethod.addItem(m)
        for c in self._popClasses:
            self._ui.comboBoxClass.addItem(c)

    def accept(self):
        '''
        Override the accept method so that we can confirm saving an
        invalid configuration.
        '''
        result = QtGui.QMessageBox.Yes
        if not self.validate():
            result = QtGui.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', are you sure you want to save this configuration?)',
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if result == QtGui.QMessageBox.Yes:
            QtGui.QDialog.accept(self)

    def validate(self):
        '''
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the 
        overall validity of the configuration.
        '''
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        return valid

    def getConfig(self):
        '''
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = self._ui.lineEdit0.text()
        config = {}
        config['identifier'] = self._ui.lineEdit0.text()
        config['Prediction Method'] = self._ui.comboBoxMethod.currentText()
        config['Population Class'] = self._ui.comboBoxClass.currentText()
        config['LASIS'] = self._ui.lineEditLASIS.text()
        config['RASIS'] = self._ui.lineEditRASIS.text()
        config['LPSIS'] = self._ui.lineEditLPSIS.text()
        config['RPSIS'] = self._ui.lineEditRPSIS.text()
        config['PS'] = self._ui.lineEditPS.text()
        config['GUI'] = self._ui.checkBoxGUI.isChecked()
        return config

    def setConfig(self, config):
        '''
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        '''
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        self._ui.comboBoxMethod.setCurrentIndex(self._methods.index(config['Prediction Method']))
        self._ui.comboBoxClass.setCurrentIndex(self._popClasses.index(config['Population Class']))
        self._ui.lineEditLASIS.setText(config['LASIS'])
        self._ui.lineEditRASIS.setText(config['RASIS'])
        self._ui.lineEditLPSIS.setText(config['LPSIS'])
        self._ui.lineEditRPSIS.setText(config['RPSIS'])
        self._ui.lineEditPS.setText(config['PS'])
        self._ui.checkBoxGUI.setChecked(bool(config['GUI']))

