import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { AddpostRoutingModule } from './addpost-routing.module';
import { AddpostsComponent } from './addpost.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    AddpostRoutingModule,
    ReactiveFormsModule,
    CommonModule
  ],
  declarations: [AddpostsComponent]
})
export class AppModule { }
