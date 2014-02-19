Lexor Language: XML to XML default style converter
==================================================

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
