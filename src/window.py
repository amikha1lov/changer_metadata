# window.py
#
# Copyright 2020 ivan-tretyak
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from .pdf import PDF
from locale import gettext as _
import os


@Gtk.Template(resource_path='/com/github/ivantretyak/changemetadapdf/ui/about.ui')
class About_dialog(Gtk.AboutDialog):

   __gtype_name__ = "_about_dialog"

   def __init__(self, **kwargs):
        super().__init__(**kwargs)



@Gtk.Template(resource_path='/com/github/ivantretyak/changemetadapdf/ui/window.ui')
class ChangemetadapdfWindow(Gtk.ApplicationWindow):

    __gtype_name__ = 'ChangemetadapdfWindow'

    _file_chooser_button = Gtk.Template.Child()
    _save_button = Gtk.Template.Child()

    _author = Gtk.Template.Child()
    _keyword = Gtk.Template.Child()
    _title = Gtk.Template.Child()
    _subject = Gtk.Template.Child()

    _headerbar = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pdf = None



    @Gtk.Template.Callback()
    def on__file_chooser_button_clicked(self, button):
        dialog = self.__file_chooser_dialog()
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            f = dialog.get_filename()
            dialog.destroy()
            self._headerbar.set_title(os.path.basename(f))
            self.pdf = PDF(f)
            self.__set_metadata_field(self.pdf)
            return 0
        else:
            print(dialog)
            dialog.destroy()
        del response



    @Gtk.Template.Callback()
    def on__save_button_clicked(self, button):
        values = []
        info = {}
        values.append(self._author.get_text())
        values.append(self._keyword.get_text())
        values.append(self._title.get_text())
        values.append(self._subject.get_text())
        for i in range(len(values)):
            info.update({self.pdf.keys[i]:values[i]})
        self.pdf.update_metadata(info)
        del values, info



    @Gtk.Template.Callback()
    def on__about_button_clicked(self, button):
        print('stetst')
        response = About_dialog()
        response.run()
        if response == Gtk.ResponseType.OK:
            response.destroy()
        else:
            response.destroy()
        del response

    def __add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.add_mime_type("application/pdf")
        dialog.add_filter(filter_text)


    def __set_metadata_field(self, file_pdf:PDF):
        self._author.set_text(file_pdf.author())
        self._keyword.set_text(file_pdf.keyword())
        self._title.set_text(file_pdf.title())
        self._subject.set_text(file_pdf.subject())

    def __file_chooser_dialog(self):
        dialog  = Gtk.FileChooserDialog(_("Choose a file"), None, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.__add_filters(dialog)
        return dialog
