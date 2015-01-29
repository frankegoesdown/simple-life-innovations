#from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
#from parse.models import Sites

import queue
import threading
import urllib
import time
from bs4 import BeautifulSoup


HOSTS = ["http://ya.ru", "https://python.org", "https://ru.wikipedia.org"]

QUEUE = queue.Queue()
OUT_QUEUE = queue.Queue()
TITLES = []


class ThreadUrl(threading.Thread):
	"""Threaded Url Grab"""

	def __init__(self, queue, out_queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.out_queue = out_queue

	def run(self):
		while True:
			# grabs host from queue
			host = self.queue.get()

			#grabs urls of hosts and then grabs chunk of webpage
			url = urllib.request.urlopen(host)
			chunk = url.read()

			#place chunk into out queue
			self.out_queue.put(chunk)

			#signals to queue job is done
			self.queue.task_done()


class DatamineThread(threading.Thread):
	"""Threaded Url Grab"""

	def __init__(self, out_queue):
		threading.Thread.__init__(self)
		self.out_queue = out_queue

	def run(self):
		list = []
		while True:
			# grabs host from queue
			chunk = self.out_queue.get()

			#parse the chunk
			soup = BeautifulSoup(chunk)
			TITLES.append(soup.title.string)

			#signals to queue job is done
			#list.append(some)
			self.out_queue.task_done()
		#print list


start = time.time()


def main():
	# spawn a pool of threads, and pass them queue instance

	for i in range(5):
		t = ThreadUrl(QUEUE, OUT_QUEUE)
		t.setDaemon(True)
		t.start()

	#populate queue with data
	for host in HOSTS:
		QUEUE.put(host)

	for i in range(5):
		dt = DatamineThread(OUT_QUEUE)
		dt.setDaemon(True)
		dt.start()


	#wait on the queue until everything has been processed
	QUEUE.join()
	OUT_QUEUE.join()


def parse(request):
	main()
	titles = TITLES
	elapsed_time = "Elapsed Time: %s" % (time.time() - start)
	return render_to_response('parse.html', locals())
