import time 

print('Downloading', end='')
for n in range(20):
    print('.', end='', flush=True)
    time.sleep(0.3)
print('\nDownloading completed!')