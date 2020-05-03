import { Validators } from '@angular/forms';

export const enquiries_ValidatorGroups = {
    tenantName:[
            Validators.required,
    ],
    bedsId:[
            Validators.required,
    ],
    tenantId:[
            Validators.required,
    ],
    roomsId:[
            Validators.required,
    ],
    roomType:[
            Validators.required,
    ],
    roomGender:[
            Validators.required,
    ],
    numberPeople:[
            Validators.required,
    ],
    duration:[
            Validators.required,
    ],
    startDate:[
            Validators.required,
    ],
    maxRent:[
            Validators.required,
    ],
    message:[
            Validators.required,
    ],
    propertyId:[
            Validators.required,
    ],
    
};

export const enquiries_ValidatorMessages = {
  tenantName: {
    
    required: "tenantName is something else"
    
  },
  bedsId: {
    
    required: "bedsId is something else"
    
  },
  tenantId: {
    
    required: "tenantId is something else"
    
  },
  roomsId: {
    
    required: "roomsId is something else"
    
  },
  roomType: {
    
    required: "roomType is something else"
    
  },
  roomGender: {
    
    required: "roomGender is something else"
    
  },
  numberPeople: {
    
    required: "numberPeople is something else"
    
  },
  duration: {
    
    required: "duration is something else"
    
  },
  startDate: {
    
    required: "startDate is something else"
    
  },
  maxRent: {
    
    required: "maxRent is something else"
    
  },
  message: {
    
    required: "message is something else"
    
  },
  propertyId: {
    
    required: "propertyId is something else"
    
  },
  
};


export const enquiriesForm = {
    tenantName: {
        tenantName: [null,enquiriesValidatorGroups.enquiries.tenantName],
      },
      bedsId: {
        bedsId: [null,enquiriesValidatorGroups.enquiries.bedsId],
      },
      tenantId: {
        tenantId: [null,enquiriesValidatorGroups.enquiries.tenantId],
      },
      roomsId: {
        roomsId: [null,enquiriesValidatorGroups.enquiries.roomsId],
      },
      roomType: {
        roomType: [null,enquiriesValidatorGroups.enquiries.roomType],
      },
      roomGender: {
        roomGender: [null,enquiriesValidatorGroups.enquiries.roomGender],
      },
      numberPeople: {
        numberPeople: [null,enquiriesValidatorGroups.enquiries.numberPeople],
      },
      duration: {
        duration: [null,enquiriesValidatorGroups.enquiries.duration],
      },
      startDate: {
        startDate: [null,enquiriesValidatorGroups.enquiries.startDate],
      },
      maxRent: {
        maxRent: [null,enquiriesValidatorGroups.enquiries.maxRent],
      },
      message: {
        message: [null,enquiriesValidatorGroups.enquiries.message],
      },
      propertyId: {
        propertyId: [null,enquiriesValidatorGroups.enquiries.propertyId],
      },
      
};