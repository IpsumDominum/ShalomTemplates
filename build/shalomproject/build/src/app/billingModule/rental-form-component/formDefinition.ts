import { Validators } from '@angular/forms';

export const bookings_ValidatorGroups = {
    rentalName:[
            Validators.required,
    ],
    rentalBooked:[
            Validators.required,
    ],
    rentalDate:[
            Validators.required,
    ],
    rentalHello:[
            Validators.required,
    ],
    
};

export const bookings_ValidatorMessages = {
  rentalName: {
    
    required: "rentalName is something else"
    
  },
  rentalBooked: {
    
    required: "rentalBooked is something else"
    
  },
  rentalDate: {
    
    required: "rentalDate is something else"
    
  },
  rentalHello: {
    
    required: "rentalHello is something else"
    
  },
  
};


export const bookingsForm = {
    rentalName: {
        rentalName: [null,rentalValidatorGroups.rental.rentalName],
      },
      rentalBooked: {
        rentalBooked: [null,rentalValidatorGroups.rental.rentalBooked],
      },
      rentalDate: {
        rentalDate: [null,rentalValidatorGroups.rental.rentalDate],
      },
      rentalHello: {
        rentalHello: [null,rentalValidatorGroups.rental.rentalHello],
      },
      
};