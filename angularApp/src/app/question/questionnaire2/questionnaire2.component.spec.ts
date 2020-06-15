import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Questionnaire2Component } from './questionnaire2.component';

describe('Questionnaire2Component', () => {
  let component: Questionnaire2Component;
  let fixture: ComponentFixture<Questionnaire2Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Questionnaire2Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Questionnaire2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
