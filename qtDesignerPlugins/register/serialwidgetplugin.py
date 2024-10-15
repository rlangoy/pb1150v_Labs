"""
serialwidgetplugin.py

"""
from PyQt6.QtGui import QIcon,QPixmap,QImage
from PyQt6.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt6.QtCore import QByteArray

from serialwidget import SerialTerminalWidget

class SerialWidgetPlugin(QPyDesignerCustomWidgetPlugin):
    """SerialWidgetPlugin(QPyDesignerCustomWidgetPlugin)
    
    Provides a Python custom plugin for Qt Designer by implementing the
    QDesignerCustomWidgetPlugin via a PyQt-specific custom plugin class.
    """

    # The __init__() method is only used to set up the plugin and define its
    # initialized variable.
    def __init__(self, parent=None):
    
        super().__init__(parent)

        self.initialized = False

    # The initialize() and isInitialized() methods allow the plugin to set up
    # any required resources, ensuring that this can only happen once for each
    # plugin.
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    # This factory method creates new instances of our custom widget with the
    # appropriate parent.
    def createWidget(self, parent):
        return SerialTerminalWidget(parent)

    # This method returns the name of the custom widget class that is provided
    # by this plugin.
    def name(self):
        return "SerialTerminalWidget"

    # Returns the name of the group in Qt Designer's widget box that this
    # widget belongs to.
    def group(self):
        return "PyQt Examples"

    # Returns the icon used to represent the custom widget in Qt Designer's
    # widget box.
    def icon(self):
        return QIcon(QPixmap.fromImage(self.qImgConnected))

    # Returns a short description of the custom widget for use in a tool tip.
    def toolTip(self):
        return ""

    # Returns a short description of the custom widget for use in a "What's
    # This?" help message for the widget.
    def whatsThis(self):
        return ""

    # Returns True if the custom widget acts as a container for other widgets;
    # otherwise returns False. Note that plugins for custom containers also
    # need to provide an implementation of the QDesignerContainerExtension
    # interface if they need to add custom editing support to Qt Designer.
    def isContainer(self):
        return False

    # Returns an XML description of a custom widget instance that describes
    # default values for its properties. Each custom widget created by this
    # plugin will be configured using this description.
    def domXml(self): return """
        <widget class="SerialTerminalWidget" name="serialwidget" >\n
            <property name="geometry"> 
                <rect>  <x> 0 </x> 
                        <y> 0 </y>  
                        <width> 164 </width> 
                        <height> 42 </height> 
                </rect>   
            </property> 
        </widget>
        """

    #    return '<widget class="SerialTerminalWidget" name="serialwidget" />\n'  \
    #    '<property name="geometry"> '  \
    #    '<rect> <x> 0 </x> <y> 0 </y>  <width> 100 </width> <height> 55 </height> </rect> ' \
    #    '</property>\n' \
    #    '</widget>\n'


    # Returns the module containing the custom widget class. It may include
    # a module path.
    def includeFile(self):
        return "serialwidget"

    electrical_services_svg = """
    <svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px" fill="#5f6368"><path d="M716.67-360v-66.67h90q14.33 0 23.83 9.5 9.5 9.5 9.5 23.84 0 13.66-9.5 23.5Q821-360 806.67-360h-90Zm0 160v-66.67h90q14.33 0 23.83 9.5 9.5 9.5 9.5 23.84 0 13.66-9.5 23.5Q821-200 806.67-200h-90ZM560-160q-30.33 0-51.83-23.5t-21.5-56.5h-90v-146.67h90q0-33 21.5-56.5t51.83-23.5h123.33V-160H560ZM276.67-280Q210-280 165-324.67q-45-44.66-45-112 0-67.33 45-112 45-44.66 111.67-44.66H340q30.33 0 50.17-19.84Q410-633 410-663.33q0-30.34-19.83-50.17-19.84-19.83-50.17-19.83H193.33q-13.66 0-23.5-9.84Q160-753 160-766.67q0-14.33 9.83-23.83 9.84-9.5 23.5-9.5H340q58 0 97.33 39.33 39.34 39.34 39.34 97.34T437.33-566Q398-526.67 340-526.67h-63.33q-39 0-64.5 25.17t-25.5 64.83q0 39.67 25.5 64.84 25.5 25.16 64.5 25.16h86.66V-280h-86.66Z"/></svg>
    """
    qImgConnected=QImage.fromData(QByteArray(electrical_services_svg.encode('utf-8')))
