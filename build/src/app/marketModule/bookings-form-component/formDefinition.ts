import { Validators } from '@angular/forms';

export const bookings_ValidatorGroups = {
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

export const bookings_ValidatorMessages = {
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


export const bookingsForm = {
    tenantName: {
        tenantName: [null,bookingsValidatorGroups.bookings.tenantName],
      },
      bedsId: {
        bedsId: [null,bookingsValidatorGroups.bookings.bedsId],
      },
      tenantId: {
        tenantId: [null,bookingsValidatorGroups.bookings.tenantId],
      },
      roomsId: {
        roomsId: [null,bookingsValidatorGroups.bookings.roomsId],
      },
      roomType: {
        roomType: [null,bookingsValidatorGroups.bookings.roomType],
      },
      roomGender: {
        roomGender: [null,bookingsValidatorGroups.bookings.roomGender],
      },
      numberPeople: {
        numberPeople: [null,bookingsValidatorGroups.bookings.numberPeople],
      },
      duration: {
        duration: [null,bookingsValidatorGroups.bookings.duration],
      },
      startDate: {
        startDate: [null,bookingsValidatorGroups.bookings.startDate],
      },
      maxRent: {
        maxRent: [null,bookingsValidatorGroups.bookings.maxRent],
      },
      message: {
        message: [null,bookingsValidatorGroups.bookings.message],
      },
      propertyId: {
        propertyId: [null,bookingsValidatorGroups.bookings.propertyId],
      },
      
};