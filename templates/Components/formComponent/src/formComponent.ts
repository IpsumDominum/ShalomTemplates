import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup } from '@angular/forms';
import { FormService, {{capitalize(componentName)}}Service, AuthService} from '../../../shared/services';
import { SelectOptions } from '../../billing-shared';
import { {{capitalize(componentName)}}Item } from '../../../shared/models';
import { takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { promise } from 'protractor';

@Component({
  selector: 'app-{{componentName}}-form',
  templateUrl: './{{componentName}}-form.component.html'
})
export class {{capitalize(componentName)}}FormComponent implements OnInit, OnDestroy {

  {{componentName}}: {{capitalize(componentName)}}Item;
  unsubscribe: Subject<void> = new Subject<void>();
  loading: boolean = true;
  isNew:boolean;
  {{componentName}}Form: FormGroup;
  formErrors: any = {};
  constructor(
    private {{componentName}}Service: {{capitalize(componentName)}}Service,
    private formService: FormService,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
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
    this.{{componentName}}Form = this.formBuilder.group(this.formService.formBuilds.{{componentName}}Form);
    this.{{componentName}}Form.valueChanges.pipe(takeUntil(this.unsubscribe)).subscribe(() => {
      this.formErrors = this.formService.getErrors(this.{{componentName}}Form);
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
    const form_grabbed = this.{{componentName}}.value;
    form_grabbed.accountId = this.authService.getAccountId();
    if (this.isNew) {
      this.{{componentName}}Service.create{{componentName}}(form_grabbed).then((result) => {
        this.router.navigateByUrl('/...route to be replaced..../view/' + result);
      });
    } else {
      form_grabbed.{{componentName}}Id = this.{{componentName}}.{{componentName}}Id;
      this.{{componentName}}Service.updateEnquiries(form_grabbed).then(() => {
        this.router.navigateByUrl('/...route to be replaced..../view/' + this.{{componentName}}.{{componentName}}Id);
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