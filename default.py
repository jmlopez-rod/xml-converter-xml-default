"""XML to XML DEFAULT Converter Style

Copies the xml file and evaluates the python instructions. This
evaluation may be stopped by modifying the option `exec`. For
instance, suppose we have the file `example.xml`

    <!--file example.xml-->
    <message>
    <?python
    import lexor.core.elements as core
    print 'This message gets printed last.'
    echo('This message gets printed first.')
    echo(core.Void('br'))
    ?>
    </message>

Using the defaults we can evaluate the python code

    jmlopez$ lexor example.xml to xml
    <!--file example.xml-->
    <message>
        This message gets printed first.
        <br/>
        This message gets printed last.  \
\n    </message>

To leave it unevaluated we can set `exec` to off.

    jmlopez$ lexor example.xml to xml[_@exec=off]
    <!--file example.xml-->
    <message>
        <?python
    import lexor.core.elements as core
    print 'This message gets printed last.'
    echo('This message gets printed first.')
    echo(core.Void('br'))
    ?>
    </message>

Notice that `echo` commands will be appended to the parent node
before `print` commands.

"""

from lexor import init
from lexor.core.converter import NodeConverter
from lexor.core.parser import Parser

INFO = init(
    version=(0, 0, 1, 'final', 0),
    lang='xml',
    to_lang='xml',
    type='converter',
    description='Copy xml file and evaluate python instructions.',
    url='http://jmlopez-rod.github.io/lexor-lang/xml-converter-xml-default',
    author='Manuel Lopez',
    author_email='jmlopez.rod@gmail.com',
    license='BSD License',
    path=__file__
)
DEFAULTS = {
    'error': 'on',
    'exec': 'on',
}


class PythonNC(NodeConverter):
    """Append a node with python instructions to a list. """

    def process(self, node):
        self.converter.python.append(node)


MAPPING = {
    '?python': PythonNC,
}
PARSER = Parser('xml', 'default')


def init_converter(converter):
    """Initializes a list to hold references to python embeddings. """
    converter.python = list()


def convert(converter, _):
    """Evaluate the python embeddings. """
    err = True
    if converter.defaults['error'] in ['off', 'false']:
        err = False
    if converter.defaults['exec'] in ['on', 'true']:
        for num, node in enumerate(converter.python):
            converter.exec_python(node, num, PARSER, err)
