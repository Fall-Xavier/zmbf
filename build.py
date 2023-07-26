import os,sys,shutil
from distutils.core import setup, Extension
from Cython.Build import cythonize

class Main:
	def __init__(self):
		self.file = "zmbf.cpp"
		
	def build(self):
		print(" Sedang Proses Build, Tunggu Sampai Selesai")
		nama = self.file.split(".")[0]
		setup(
			name = self.file,
			ext_modules = cythonize(Extension(name=nama, sources=[self.file])),
			script_args = ["build_ext", "--inplace", "--force", "-j 5"]
		)
		self.clear()
		
	def clear(self):
		try: shutil.rmtree("build/")
		except:pass
		try: os.remove(self.file)
		except:pass
		self.create_run()
			
	def create_run(self):
		with open("run.py","w") as run:
			run.write("from zmbf import Menu\nMenu().menu()")
		exit(" Selesai Menginstall, Silahkan Ketik : python run.py")
	
Main().build()