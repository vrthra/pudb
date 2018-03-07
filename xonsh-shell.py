from xonsh.main import main_context, main
from xonsh.shell import Shell
import builtins

from xonsh import __version__
from xonsh.lazyasd import LazyObject, lazyobject
from xonsh.environ import DEFAULT_VALUES
from xonsh.shell import Shell
from xonsh.pretty import pretty
from xonsh.jobs import ignore_sigtstp
from xonsh.tools import setup_win_unicode_console, print_color
from xonsh.platform import HAS_PYGMENTS, ON_WINDOWS
from xonsh.codecache import run_script_with_cache, run_code_with_cache
from xonsh.xonfig import xonfig_main
from xonsh.lazyimps import pygments, pyghooks

def pudb_shell(_globals, _locals):
    with main_context(argv=['--shell-type=readline']) as shell:
        shell.execer.unload = False
        env = builtins.__xonsh_env__
        env['PROMPT'] = 'xon| '
        shell.cmdloop()
