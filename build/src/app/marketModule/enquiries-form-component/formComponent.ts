import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';
import { FormService, EnquiriesService, AuthService} from '../../../shared/services';
import { SelectOptions } from '../../billing-shared';
import { EnquiriesItem } from '../../../shared/models';
import { takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { promise } from 'protractor';

@Component({
  selector: 'app-enquiries-form',
  templateUrl: './enquiries-form.component.html'
})
export class EnquiriesFormComponent implements OnInit, OnDestroy {

  enquiries: EnquiriesItem;
  unsubscribe: Subject<void> = new Subject<void>();
  loading: boolean = true;
  isNew:boolean;
  enquiriesForm: FormGroup;
  formErrors: any = {};
  constructor(
    private enquiriesService: EnquiriesService,
    private formService: FormService,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
    private dataService: DataService
  ) { }

  ngOnInit() {
    this.load();
  }

  ngOnDestroy() {
    this.unsubscribe.next();
    this.unsubscribe.complete();
  }

  /**
   * Loads component state and data.
   * First checks for the required state of the form,
   * then retrieves any data needed for form population.
   */
  async load() {
    this.loading = true;    
    this.isNew = true; //TODO: Change it to actually checking    
    this.loading = false;
  }
  /**
   * Parses the ISO string back to form date format yy-mm-dd.
   */
  parseDate(date: any) {
    date = new Date(Date.parse(date));
    const year = date.getFullYear();
    let month = date.getMonth() + 1;
    let dt = date.getDate();
    if (dt < 10) dt = '0' + dt;
    if (month < 10) month = '0' + month;
    return year + "-" + month + "-" + dt;
  }

  /**
   * Builds the form and handles validation.
   */
  buildForm() {
    this.enquiriesForm = this.formBuilder.group(this.formService.formBuilds.enquiriesForm);
    this.enquiriesForm.valueChanges.pipe(takeUntil(this.unsubscribe)).subscribe(() => {
      this.formErrors = this.formService.getErrors(this.enquiriesForm);
    });
  }
  /**
   * Submits form data.
   */
  async submitForm() {
    this.loading = true;
    /*If want to patch value
    this.enquiriesForm.patchValue({
    });
    */
    const form_grabbed = this.enquiries.value;
    form_grabbed.accountId = this.authService.getAccountId();
    if (this.isNew) {
      this.enquiriesService.createenquiries(form_grabbed).then((result) => {
        this.router.navigateByUrl('/...route to be replaced..../view/' + result);
      });
    } else {
      form_grabbed.enquiriesId = this.enquiries.enquiriesId;
      this.enquiriesService.updateEnquiries(form_grabbed).then(() => {
        this.router.navigateByUrl('/...route to be replaced..../view/' + this.enquiries.enquiriesId);
      });
    }
    this.loading = false;
  }

  /**
   * Cancels the form
   */
  cancel() {
    this.router.navigateByUrl('/...route to be replaced..../view/all');
  }
}