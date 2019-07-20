import logging
from glob import glob
from jinjafy import Jinjafier

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    template = "project.md"
    default_meta = glob("data/meta/*.ymd") + glob("./data/meta/*.yaml")
    meta = "data/projects/merck.uldir.ymd"

    j = Jinjafier(template, default_meta=default_meta)
    o = j.render(meta)

    logging.debug(o)

