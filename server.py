import subprocess
from   threading import Thread
from   flask     import Flask, request

app = Flask(__name__)

def worker(percentage, memsize, seconds):
    memsizeInMb = str(memsize) + 'MB'
    subprocess.run(['timeout', str(seconds), '/usr/local/bin/lookbusy', '-c', str(percentage), '-m', str(memsizeInMb)])

@app.route('/')
def load(): 
    percentage = request.args.get('percentage') if "percentage" in request.args else 50
    memsize = request.args.get('memsize') if "memsize" in request.args else 128
    seconds    = request.args.get('seconds')    if "seconds"    in request.args else 10
    Thread(target=worker, args=(percentage, memsize, seconds)).start()
    return "started"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=False, processes=10)