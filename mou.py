import re, os
import sublime, sublime_plugin

file_type_reg = re.compile('(.*?)\.(md|MD|markdown)$') #only support .md .MD .markdown

class OpenWithMou(sublime_plugin.TextCommand):
    def run(self, edit, paths = [None]):
        for path in paths:
            self.open_file(self.view, path)

    def check_file_type(self, file_name):
        try:
            file_type_reg.search(file_name).group(2)
            return True;
        except Exception, e:
            return False

    def open_file(self, view, item = None):
        file_name = view.file_name()
        ret = self.check_file_type(item or file_name)
        if (ret is True):
            command = 'open -a Mou "' + file_name + '"'
            os.system(command)