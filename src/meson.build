pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'ChangeMetadaPDF')
gnome = import('gnome')

gnome.compile_resources('ChangeMetadaPDF',
  'ChangeMetadaPDF.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'ChangeMetadaPDF.in',
  output: 'ChangeMetadaPDF',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

ChangeMetadaPDF_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'pdf.py',
]

install_data(ChangeMetadaPDF_sources, install_dir: moduledir)
