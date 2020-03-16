import { Validators } from '@angular/forms';

export const bookings_ValidatorGroups = {
    {% for m in model %}{{m.name}}:[
            Validators.required,
    ],
    {% endfor %}
};

export const bookings_ValidatorMessages = {
  {% for m in model %}{{m.name}}: {
    {% if m.type=="boolean" %}
    required: "{{m.name}} has to be a boolean"
    {% else %}
    required: "{{m.name}} is something else"
    {% endif %}
  },
  {% endfor %}
};


export const bookingsForm = {
    {% for m in model %}{{m.name}}: {
        {{m.name}}: [null,{{componentName}}ValidatorGroups.{{componentName+"."+m.name}}],
      },
      {% endfor %}
};
