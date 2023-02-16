# encoding:utf-8
from requests.sessions import session
from common.get_secrets import get_secrets


# 重写请求方法,便于直接获取结果
class DYHTTPRequests:

    def __init__(self):
#         self.cookie = get_secrets('COOKIES')
        self.cookie = "dy_did=f9f5c9ffc5be84b46faa895500031601; acf_did=f9f5c9ffc5be84b46faa895500031601; dy_did=f9f5c9ffc5be84b46faa895500031601; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1675346992,1675939362; PHPSESSID=j568f7sub8ufb6tpjug9lqie83; acf_avatar=https://apic.douyucdn.cn/upload/avatar_v3/202003/947f800e395d48b1b0941f6d04c9614e_; acf_auth=90beHcilm6o1JrCF777Lc5/hn1oHjX+1llHAeTtjhH0vPFhYGntZYi4C4rEM0mso50UVU85J0KooR1/NyZnltcPZP09/UlrqHNw7x7BsGJZBSvA2idVB0A; dy_auth=a3174yMm95UJxSkQSKSYM1UXbn5uRaKBNrE3eNtMVSJgRfbYNr9vmlPe3okdSb+4jmKjWuHb82JPss4ldZYml2ftZdjUnDKdRoCo7TOglj6aA8qVWsBmRQ; wan_auth37wan=c8d203080b7ch4gzAAJzg0jmBcE+36xCWEuvZIcCytsuvog3LJKX0F4kvXMUFrygDRbpKoUNzXEKq9zNbe95/F78zzNvAk8bbZD07YkoH3l8G3g; acf_uid=646956; acf_username=qq_sSXh6454; acf_nickname=完美小江; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=45370323; acf_biz=1; acf_stk=da5737200db432a7; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1676547889"
        self.session = session()
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
            "referer": "https://www.douyu.com",
            "Cookie": self.cookie.encode('utf-8')
        }

    def request(self, method, path, **kwargs):
        url = "https://www.douyu.com" + path
        method.upper()
        return self.session.request(method, url=url, headers=self.header, **kwargs)

    def __del__(self):
        self.session.close()


dyreq = DYHTTPRequests()
if __name__ == '__main__':
    print(dyreq.request("get", "/lapi/member/api/getInfo").json())
    glow_url = "/japi/prop/backpack/web/v1?rid=12306"
    print(dyreq.request("get", glow_url).json())
