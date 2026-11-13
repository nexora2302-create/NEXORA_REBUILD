import re
_SPLIT = re.compile(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)', re.S)
def fr_typo(html):
    out = []
    for part in _SPLIT.split(html):
        if not part or part.startswith('<'):
            out.append(part); continue
        p = re.sub(r' ([?!;])', ' \\1', part)
        p = re.sub(r' :', ' :', p)
        p = p.replace('« ', '« ').replace(' »', ' »')
        out.append(p)
    return ''.join(out)
