from subprocess import call

p = "cs_at_the_hospital"

jinjafy_binary = "/anaconda3/envs/jinjafy/bin/jinjafy"
projects = {

    "cs_at_the_hospital": {
        "meta": "merck.cs_at_the_hospital.yaml",
        "template": "revealjs_template.md",
        "from": "md",
        "to": "revealjs"
    }

}

extensions = {
    "revealjs": "html"
}

theme_maps = {
    "solarized": "light",
    "white":     "light",
    "simple":    "white",
    "night":     "dark",
    "black":     "dark"
}

config = projects[p]

jargs = ["templates/{}".format(config["template"]),
        "data/{}".format(config["meta"]),
        "-f", config["from"],
        "-t", config["to"] ]

for theme, theme_map in theme_maps.items():

    out_file = "{}-{}.{}".format(p, theme, extensions[config["to"]])
    jjargs = ["-o", "docs/{}-{}.{}".format(p, theme, extensions[config["to"]]),
              "--theme", theme]

    call([jinjafy_binary, *jargs, *jjargs])
