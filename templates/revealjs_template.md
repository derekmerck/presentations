{% macro render_slide(item, level=1, bread_crumbs='') -%}

{{ '#'*level }} {{ bread_crumbs }}{{ item.title }}{{ ' - ' if item.get('title_modifier') }}{{ item.title_modifier }}

{% if item.get('image') -%}

::: columns
:::: {.column width={{ '60%' if not item.get("wide_image") else '40%'}} }
{{ item.content }}
::::
:::: {.column width={{ '40%' if not item.get("wide_image") else '60%'}}}

::::: {.fig}
![{{ item.im_caption }}](images/{{ item.image }})
:::::

::::
:::

{%- elif item.get('content2') %}

::: columns
:::: {.column width=50% }
{{ item.content }}
::::
:::: {.column width=50% }
{{ item.content2 }}
::::
:::

{%- else -%}

{{ item.content }}

{%- endif %}

{% for subitem in item.children -%}
{{ render_slide(subitem, level=level+1, bread_crumbs=item.title+" - ") }}
{% endfor %}

{%- endmacro -%}

---
author: {{ author }}
title: {{ title }}
date: {{ date }}
...

<style>
div.column {
  font-size: smaller;
  vertical-align: middle;
}
div.condensed {
  font-size: smaller;
}
.reveal strong {
  color: khaki;
}
.reveal figcaption {
  font-size: 50%;
  color: white;
}
</style>

{% for item in content -%}
{{ render_slide(item, level=2) }}
{% endfor %}
