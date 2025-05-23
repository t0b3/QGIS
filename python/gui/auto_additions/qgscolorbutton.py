# The following has been generated automatically from src/gui/qgscolorbutton.h
QgsColorButton.Behavior.baseClass = QgsColorButton
try:
    QgsColorButton.__attribute_docs__ = {'colorChanged': 'Emitted whenever a new color is set for the button. The color is always\nvalid. In case the new color is the same no signal is emitted, to avoid\ninfinite loops.\n\n:param color: New color\n', 'colorClicked': "Emitted when the button is clicked, if the button's behavior is set to\nSignalOnly\n\n:param color: button color\n\n.. seealso:: :py:func:`setBehavior`\n\n.. seealso:: :py:func:`behavior`\n", 'cleared': 'Emitted when the color is cleared (set to null).\n\n.. seealso:: :py:func:`setToNull`\n\n.. versionadded:: 3.12\n', 'unlinked': 'Emitted when the color is unlinked, e.g. when it was previously set to\nlink to a project color and is now no longer linked.\n\n.. seealso:: :py:func:`unlink`\n\n.. seealso:: :py:func:`linkToProjectColor`\n\n.. versionadded:: 3.6\n'}
    QgsColorButton.createMenuIcon = staticmethod(QgsColorButton.createMenuIcon)
    QgsColorButton.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'event', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'keyPressEvent', 'dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'wheelEvent']
    QgsColorButton.__signal_arguments__ = {'colorChanged': ['color: QColor'], 'colorClicked': ['color: QColor']}
except (NameError, AttributeError):
    pass
