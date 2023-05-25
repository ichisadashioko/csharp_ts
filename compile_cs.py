import os
import sys
import subprocess

base_filepath = 'C:/Windows/Microsoft.NET/Framework64'
base_filepath = os.path.abspath(base_filepath)

child_filename_list = os.listdir(base_filepath)

dotnet_v4_root_dirname = None
for child_filename in child_filename_list:
  if child_filename.upper().startswith('V4.0'):
    dotnet_v4_root_dirname = child_filename
    break
if dotnet_v4_root_dirname is None:
  raise Exception('cannot find dotnet v4')
csc_filepath = os.path.join(base_filepath, dotnet_v4_root_dirname, 'csc.exe')
pwd = os.path.abspath(os.getcwd())
output_filepath = os.path.join(pwd, 'ts.exe')
compile_command = f'{csc_filepath} /optimize /target:winexe /platform:x64 /out:"{output_filepath}" Program.cs'
sp = subprocess.Popen(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_bs, stderr_bs = sp.communicate()

sys.stdout.buffer.write(stdout_bs)
sys.stderr.buffer.write(stderr_bs)

os.exit(sp.returncode)
