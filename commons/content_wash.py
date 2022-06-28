# coding=gbk


import re


# ��ϴ���ݲ���
re_charEntity = re.compile(r'&#?(?P<name>\w+);')


def replace_char_entity(htmlstr):
    """
    �滻����HTML�ַ�ʵ��.
    ʹ���������ַ��滻HTML��������ַ�ʵ��.
     ���������µ�ʵ���ַ���CHAR_ENTITIES��,�������HTML�ַ�ʵ��.
     @param htmlstr HTML�ַ���.
    """
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"', }

    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entityȫ�ƣ���>
        key = sz.group('name')  # ȥ��&;��entity,��>Ϊgt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # �Կմ�����
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


##����HTML�еı�ǩ
# ��HTML�б�ǩ����Ϣȥ��
# @param htmlstr HTML�ַ���.
def filter_tags(htmlstr):
    # �ȹ���CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # ƥ��CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # ������
    re_h = re.compile('</?\w+[^>]*>')  # HTML��ǩ
    re_comment = re.compile('<!--[^>]*-->')  # HTMLע��
    s = re_cdata.sub('', htmlstr)  # ȥ��CDATA
    s = re_script.sub('', s)  # ȥ��SCRIPT
    s = re_style.sub('', s)  # ȥ��style
    s = re_br.sub('\n', s)  # ��brת��Ϊ����
    s = re_h.sub('', s)  # ȥ��HTML ��ǩ
    s = re_comment.sub('', s)  # ȥ��HTMLע��
    # ȥ������Ŀ���
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = s.replace('\n', '')  # ȥ������
    s = s.replace(' ', '')  # ȥ��\t
    s = replace_char_entity(s)
    return s.replace('\n', '').replace('\t', '')
