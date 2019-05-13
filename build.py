from subprocess import call
import logging

p = "cs_at_the_hospital"
# p = "rih3dlab_update_0519"

jinjafy_binary = "/anaconda3/envs/jinjafy/bin/jinjafy"
projects = {

    "cs_at_the_hospital": {
        "meta": "merck.cs_at_the_hospital.yaml",
        "template": "revealjs_2d",
        "to": "revealjs"
    },

    "rih3dlab_update_0519": {
        "meta": "merck.rih3dlab_update.0519.yaml",
        "template": "revealjs_2d",
        "to": "revealjs"
    }

}

extensions = {
    "revealjs": "html"
}

themes = ["light",
    "dark",
    "black",
    "white",
    "league",
    "beige",
    "sky",
    "night",
    "serif",
    "solarized",
    "moon",
    "blood",
    "moon"
]

config = projects[p]

jargs = [config["template"],
        "data/{}".format(config["meta"]),
        "-t", config["to"] ]

# logging.basicConfig(level=logging.DEBUG)

for theme in themes:

    out_file = "{}-{}.{}".format(p, theme, extensions[config["to"]])
    jjargs = ["-o", "docs/{}-{}.{}".format(p, theme, extensions[config["to"]]),
              "--theme", theme]

    # logging.debug([*jargs, *jjargs])

    call([jinjafy_binary, *jargs, *jjargs])
