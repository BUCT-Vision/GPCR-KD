import sys;
total=100000

for i in range(0,total):
  percent=float(i)*100/float(total)
  sys.stdout.write("%.4f"%percent);
  sys.stdout.write("%\r");
  sys.stdout.flush();
  sys.stdout.write("100%!finish!\r");



print("hahah")