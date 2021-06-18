
class Post:
    def __init__(self, post):
        self.no = post['no']                         if 'no'             in post else None
        self.sticky = post['sticky']                 if 'sticky'         in post else None
        self.closed = post['closed']                 if 'closed'         in post else None
        self.now = post['now']                       if 'now'            in post else None
        self.name = post['name']                     if 'name'           in post else None
        self.sub = post['sub']                       if 'sub'            in post else None
        self.com = post['com']                       if 'com'            in post else None
        self.filename = post['filename']             if 'filename'       in post else None
        self.ext = post['ext']                       if 'ext'            in post else None
        self.w = post['w']                           if 'w'              in post else None
        self.h = post['h']                           if 'h'              in post else None
        self.tn_w = post['tn_w']                     if 'tn_w'           in post else None
        self.tn_h = post['tn_h']                     if 'tn_h'           in post else None
        self.tim = post['tim']                       if 'tim'            in post else None
        self.time = post['time']                     if 'time'           in post else None
        self.md5 = post['md5']                       if 'md5'            in post else None
        self.filesize = post['filesize']             if 'filesize'       in post else None
        self.resto = post['resto']                   if 'resto'          in post else None
        self.capcode = post['capcode']               if 'capcode'        in post else None
        self.semantic_url = post['semantic_url']     if 'semantic_url'   in post else None
        self.trip = post['trip']                     if 'trip'           in post else None
        self.id = post['id']                         if 'id'             in post else None
        self.country = post['country']               if 'country'        in post else None
        self.country_name = post['country_name']     if 'country_name'   in post else None
        self.board_flag = post['board_flag']         if 'board_flag'     in post else None
        self.flag_name = post['flag_name']           if 'flag_name'      in post else None
        self.filedeleted = post['filedelete']        if 'filedelete'     in post else None
        self.spoiler = post['spoiler']               if 'spoiler'        in post else None
        self.custom_spoiler = post['custom_spoiler'] if 'custom_spoiler' in post else None
        self.replies = post['replies']               if 'replies'        in post else None
        self.bumplimit = post['bumplimit']           if 'bumplimit'      in post else None
        self.since4pass = post['since4pass']         if 'since4pass'     in post else None
        self.unique_ips = post['unique_ips']         if 'unique_ips'     in post else None
        self.archived = post['archived']             if 'archived'       in post else None
        self.archived_on = post['archived_on']       if 'archived_on'    in post else None


