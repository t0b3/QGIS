# The following has been generated automatically from src/gui/maptools/qgsmaptool.h
QgsMapTool.Transient = QgsMapTool.Flag.Transient
QgsMapTool.EditTool = QgsMapTool.Flag.EditTool
QgsMapTool.AllowZoomRect = QgsMapTool.Flag.AllowZoomRect
QgsMapTool.ShowContextMenu = QgsMapTool.Flag.ShowContextMenu
QgsMapTool.Flags = lambda flags=0: QgsMapTool.Flag(flags)
from enum import Enum


def _force_int(v): return int(v.value) if isinstance(v, Enum) else v


QgsMapTool.Flag.__bool__ = lambda flag: bool(_force_int(flag))
QgsMapTool.Flag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsMapTool.Flag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsMapTool.Flag.__or__ = lambda flag1, flag2: QgsMapTool.Flag(_force_int(flag1) | _force_int(flag2))
try:
    QgsMapTool.__attribute_docs__ = {'messageEmitted': 'Emitted when a ``message`` should be shown to the user in the\napplication message bar.\n\n.. seealso:: :py:func:`messageDiscarded`\n', 'messageDiscarded': 'Emitted when the previous message from the tool should be cleared from\nthe application message bar.\n\n.. seealso:: :py:func:`messageEmitted`\n', 'activated': 'Emitted when the map tool is activated.\n\n.. seealso:: :py:func:`deactivated`\n', 'deactivated': 'Emitted when the map tool is deactivated.\n\n.. seealso:: :py:func:`activated`\n', 'reactivated': 'Emitted when the map tool is activated, while it is already active.\n\n.. versionadded:: 3.32\n'}
    QgsMapTool.searchRadiusMM = staticmethod(QgsMapTool.searchRadiusMM)
    QgsMapTool.searchRadiusMU = staticmethod(QgsMapTool.searchRadiusMU)
    QgsMapTool.__virtual_methods__ = ['flags', 'canvasMoveEvent', 'canvasDoubleClickEvent', 'canvasPressEvent', 'canvasReleaseEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'gestureEvent', 'canvasToolTipEvent', 'setCursor', 'activate', 'deactivate', 'reactivate', 'clean', 'populateContextMenu', 'populateContextMenuWithEvent']
    QgsMapTool.__signal_arguments__ = {'messageEmitted': ['message: str', 'level: Qgis.MessageLevel = Qgis.MessageLevel.Info']}
    QgsMapTool.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
