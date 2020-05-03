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
        tenantName: [null,rentalValidatorGroups.rental.tenantName],
      },
      bedsId: {
        bedsId: [null,rentalValidatorGroups.rental.bedsId],
      },
      tenantId: {
        tenantId: [null,rentalValidatorGroups.rental.tenantId],
      },
      roomsId: {
        roomsId: [null,rentalValidatorGroups.rental.roomsId],
      },
      roomType: {
        roomType: [null,rentalValidatorGroups.rental.roomType],
      },
      roomGender: {
        roomGender: [null,rentalValidatorGroups.rental.roomGender],
      },
      numberPeople: {
        numberPeople: [null,rentalValidatorGroups.rental.numberPeople],
      },
      duration: {
        duration: [null,rentalValidatorGroups.rental.duration],
      },
      startDate: {
        startDate: [null,rentalValidatorGroups.rental.startDate],
      },
      maxRent: {
        maxRent: [null,rentalValidatorGroups.rental.maxRent],
      },
      message: {
        message: [null,rentalValidatorGroups.rental.message],
      },
      propertyId: {
        propertyId: [null,rentalValidatorGroups.rental.propertyId],
      },
      
};