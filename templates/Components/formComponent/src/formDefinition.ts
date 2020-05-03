import { Validators } from '@angular/forms';

export const {{componentName}}_ValidatorGroups = {
    {% for m in model %}{{m.name}}:[
            Validators.required,
    ],
    {% endfor %}
};

export const {{componentName}}_ValidatorMessages = {
  {% for m in model %}{{m.name}}: {
    {% if m.type=="boolean" %}
    required: "{{m.name}} has to be a boolean"
    {% else %}
    required: "{{m.name}} is something else"
    {% endif %}
  },
  {% endfor %}
};


export const {{componentName}}Form = {
    {% for m in model %}{{m.name}}: {
        {{m.name}}: [null,{{componentName}}_ValidatorGroups.{{m.name}}],
      },
      {% endfor %}
};
