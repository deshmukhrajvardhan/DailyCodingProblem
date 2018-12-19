import sysv_ipc
import threading
from multiprocessing import Process, Queue
import sys
import errno
import timeit
from string import ascii_letters, digits
import read_mpd
import urllib
import random
import os


def write_msg(list_cmd, mq):
    for i in list_cmd:
        print(i)
        mq.send(i, True)
    return

def get_segment(segment_url):
    """ Module to download the MPD from the URL and save it to file"""
    key_c_orig_r = 262144
    key_c_orig_w = 262145
#    key_c_retx_r = 362146
#    key_c_retx_w = 462146
    #print(segment_url)
    cmd1 = [segment_url]

    try:
        mq_orig_w = sysv_ipc.MessageQueue(key_c_orig_r, sysv_ipc.IPC_CREAT, max_message_size=15000)
    except:
        print("ERROR: Queue not created")
    try:
        mq_orig_r = sysv_ipc.MessageQueue(key_c_orig_w, sysv_ipc.IPC_CREAT, max_message_size=15000)
    except:
        print("ERROR: mq_orig_r Queue not created")

    if segment_url =="-2":
        process3 = Process(target=write_msg, args=(cmd1, mq_orig_w))
        process3.start()
        process3.join()
        exit()

    chunk_number = 0
    total_data_dl_time = 0
    segment_chunk_rates=[]
    segment_size=0
    process3 = Process(target=write_msg, args=(cmd1, mq_orig_w))
    # thread3=threading.Thread(target=write_msg,args=(cmd1,mqw1))
    # thread3.start()
    process3.start()
    chunk_start_time = timeit.default_timer()
    # ipc read

    # print("Py master reading chunks")
    while True:
        (message, prior) = mq_orig_r.receive()
        m = message.split(b':')
        # print("Reply:{}, content-length:{}\n".format(message,m[1]))
        # chunk_sizes.append(float(m[1]))
        if m[0] != b'end':
            segment_size += float(m[1])
            timenow = timeit.default_timer()
            chunk_dl_time = timenow - chunk_start_time
            chunk_start_time = timenow
            chunk_number += 1
            total_data_dl_time += chunk_dl_time
            current_chunk_dl_rate = segment_size * 8 / total_data_dl_time
            segment_chunk_rates.append(current_chunk_dl_rate)
        else:
            break

    # content_length = chunk_sizes.pop()
    # DONE part
    with open('/dev/SQUAD/3_segs_chunk_rate_squad_libcurl_HTTP2.txt', 'a') as chk:
        chk.write("{}".format(segment_url))
        for item in segment_chunk_rates:
            chk.write(",{}".format(item))
        chk.write("\n")
    # print("{} sum:{}, content_length:{}".format(p_no,sum(chunk_sizes), content_length))

    process3.join()

def dw_segments():
    urls = ["https://10.10.3.2/www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/2sec/bunny_4219897bps/BigBuckBunny_2s13.m4s",
            "https://10.10.3.2/www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/2sec/bunny_4219897bps/BigBuckBunny_2s15.m4s",
            "https://10.10.3.2/www-itec.uni-klu.ac.at/ftp/datasets/DASHDataset2014/BigBuckBunny/2sec/bunny_4219897bps/BigBuckBunny_2s18.m4s"]
    for url in urls: 
        get_segment(url)

#get_mpd("https:
dw_segments()
