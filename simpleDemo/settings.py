# -*- coding: utf-8 -*-

# Scrapy settings for simpleDemo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'simpleDemo'

SPIDER_MODULES = ['simpleDemo.spiders']
NEWSPIDER_MODULE = 'simpleDemo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'simpleDemo (+http://www.yourdomain.com)'

# USER_AGENT = '''com.zhihu.android/Futureve/5.30.0-mr-12056 Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36
# X-Ab-Param:top_retagg=0;se_minor_onebox=d;top_feedre=1;top_is_gr=0;top_ntr=4;top_ab_validate=0;top_billread=1;top_nad=1;top_sjre=0;top_tmt=0;se_correct_ab=1;top_nuc=0;top_root_few_topic=0;top_adpar=0;top_billboard_count=1;top_nmt=0;top_tagore_topic=2;top_vds_alb_pos=0;se_wiki_box=1;top_yhgc=1;top_retag=0;se_refactored_search_index=1;top_hqt=9;top_login_card=2;top_card=-1;se_dt=1;top_feedtopiccard=1;top_f_r_nb=1;se_ingress=on;top_recall_deep_user=1;top_vd_op=0;top_rank=0;top_test_4_liguangyi=1;se_dl=1;top_free_content=-1;top_local=2;top_quality=0;top_recall_tb_long=51;top_root_mg=1;top_v_album=1;tp_discussion_feed_card_type=2;top_ac_merge=1;top_feedre_rtt=41;top_mlt_model=4;top_user_gift=0;tp_write_pin_guide=3;top_dtmt=2;top_root_web=0;top_topic_feedre=21;se_cm=1;tp_ios_topic_write_pin_guide=1;top_30=0;top_recall_tb=2;top_cc_at=1;se_auto_syn=0;top_billpic=0;top_new_feed=1;tp_discussion_feed_type_android=2;tp_favsku=a;se_relevant_query=new;top_recall_follow_user=91;top_uit=0;top_recall_tb_short=61;se_daxuechuisou=new;se_merger=1;ls_new_score=1;top_follow_reason=0;top_vdio_rew=0;se_consulting_switch=off;top_nszt=0;top_recall_tb_follow=71;se_consulting_price=p;pin_efs=orig;se_major_onebox=wiki;top_memberfree=1;se_entity=on;top_manual_tag=1;top_recall_core_interest=81;top_ad_slot=1;top_fqai=0;top_hca=0;top_tffrt=0;se_product_rank_list=1;top_promo=1;se_gi=1;top_feedre_cpt=101;top_newfollowans=0;top_feedre_itemcf=31;top_spec_promo=1;top_videos_priority=-1;top_video_fix_position=4;pin_ef=a;top_new_user_gift=0;top_root_ac=1;top_sj=2;top_nucc=0;top_slot_ad_pos=1;top_no_weighing=1;se_rescore=1;top_alt=0;top_gr_auto_model=0;top_billvideo=0;top_recall=7;top_multi_model=0;top_distinction=3;top_ebook=0;top_tagore=1;top_tuner_refactor=-1;top_nid=0;top_gr_topic_reweight=1;top_video_rew=0;top_billab=1;top_gif=0;top_fqa=0;top_yc=1;ls_new_video=0;top_root=1;top_vd_gender=0;top_vd_rt_int=0;ls_play_continuous_order=2;top_followtop=1;top_tr=4;top_universalebook=1;se_filter=1;top_recommend_topic_card=1;top_tag_isolation=1;top_bill=0;se_tf=1;top_raf=y;top_video_score=1;top_gr_model=1;top_pfq=5;se_new_market_search=on;top_billupdate1=3;top_lowup=1;se_gemini_service=knowledge;top_newfollow=0;top_an=0;top_wonderful=1;tp_sft=a;zr_ans_rec=gbrank;top_hweb=1;top_roundtable=1'''

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'simpleDemo.middlewares.SimpledemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'simpleDemo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'simpleDemo.pipelines.SimpledemoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
