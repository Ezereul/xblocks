import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
import codejail.jail_code

class CodeExecXBlock(XBlock):
    display_name = String(
        display_name="Display Name",
        default="Code Execution",
        scope=Scope.settings,
    )

    def student_view(self, context=None):
        html = pkg_resources.resource_string(__name__, "static/html/swiftplugin.html")
        frag = Fragment(html)
        frag.add_css(pkg_resources.resource_string(__name__, "static/css/swiftplugin.css"))
        frag.add_javascript(pkg_resources.resource_string(__name__, "static/js/src/swiftplugin.js"))
        frag.initialize_js('CodeExecXBlock')
        return frag

    @XBlock.json_handler
    def execute_code(self, data, suffix=''):
        code = data.get('code', '')
        try:
            result = codejail.jail_code.jail_code('python', code)
            return {'result': result}
        except codejail.jail_code.JailedCodeException as e:
            return {'error': str(e)}

codejail.jail_code.configure("python", "/usr/bin/python3")