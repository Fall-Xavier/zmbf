import os,sys,shutil
from distutils.core import setup, Extension
from Cython.Build import cythonize

main_file = "facebook.cpp"
try:
	nama = main_file.split(".")[0]
	setup(
		name = main_file,
		ext_modules = cythonize(Extension(name=nama, sources=[main_file])),
		script_args = [
			"build_ext", "--inplace", "--force", "-j 5"]
	)
except Exception as e:
	print(e)
if os.path.exists(main_file):
	try: shutil.rmtree("build/")
	except:0
	try: os.remove(main_file)
	except:0
else:
	print("install semua module dengan mengetik : pip install -r asset/requirements.txt")

