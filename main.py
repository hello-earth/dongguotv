# -*- coding:utf-8 -*-
import base58
import requests, copy, json, urllib, random, time, platform
import sys


nheader = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}


def http_get(url, cookie=""):
    mheader = copy.deepcopy(nheader)
    if (cookie):
        mheader["Cookie"] = cookie
    conn = requests.get(url, headers=mheader)
    return conn.text


result = http_get("https://pz.v88.qzz.io/?format=2&source=jin18")
result = base58.b58decode(result)
result = json.loads(result)
if result:
    sites = []
    api_sites = result["api_site"]
    for key in api_sites:
        sites.append({"key": key, "active": True, "name": api_sites[key]["name"], "api": api_sites[key]["api"]})
    if sites:
        sites = {"sites": sites}
        with open("db.json", "wb") as fp:
            fp.write(json.dumps(sites).encode('u8'))
