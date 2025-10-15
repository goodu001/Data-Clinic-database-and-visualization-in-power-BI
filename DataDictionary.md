# 📚 Medical Clinic Power BI - Data Dictionary

## 📊 Data Model Overview

**Model Type:** Star Schema  
**Total Tables:** 11 (3 Fact Tables + 8 Dimension Tables)  
**Recommended Relationships:** 
- One-to-Many from Dimension to Fact tables
- Date table marked as Date Table in Power BI

---

## 📅 DimDate - Date Dimension

**Purpose:** Time intelligence and date-based analysis  
**Grain:** One row per day  
**Recommended as:** Date Table (mark in Power BI)

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| DateKey | Integer | Primary Key, format YYYYMMDD | 20250101 | Use for relationships |
| Date | Date | Actual date | 2025-01-01 | Display date |
| Year | Integer | Year | 2025 | For year filtering |
| Quarter | String | Quarter | Q1 | Q1-Q4 |
| Month | Integer | Month number | 1 | 1-12 |
| MonthName | String | Month name (EN) | January | English name |
| MonthNameThai | String | Month name (TH) | มกราคม | Thai name |
| Day | Integer | Day of month | 1 | 1-31 |
| DayOfWeek | Integer | Day of week | 1 | 1=Monday, 7=Sunday |
| DayName | String | Day name | Monday | English day name |
| WeekOfYear | Integer | ISO week number | 1 | 1-53 |
| IsWeekend | Integer | Weekend flag | 0 | 1=Weekend, 0=Weekday |
| FiscalYear | Integer | Fiscal year | 2025 | Adjust based on fiscal period |

**Key Relationships:**
- DateKey → FactBillingDetail.BillingDateKey
- DateKey → FactAppointment.AppointmentDateKey
- DateKey → FactPatientVisit.VisitDateKey

---

## 🏢 DimBranch - Branch/Clinic Dimension

**Purpose:** Branch analysis and geographic reporting  
**Grain:** One row per branch/clinic

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| BranchID | Integer | Primary Key | 1 | Unique branch identifier |
| BranchCode | String | Branch code | BKK-CTW | Short code |
| BranchName | String | Branch name | คลินิกเซ็นทรัลเวิลด์ | Full name |
| Region | String | Geographic region | กรุงเทพฯ | Major region |
| Province | String | Province | กรุงเทพมหานคร | Province name |
| District | String | District | ปทุมวัน | District name |
| Size | String | Branch size | Large | Small/Medium/Large |
| OpenDate | Date | Opening date | 2020-01-15 | Branch opening date |
| SquareMeter | Integer | Floor area (sqm) | 450 | Physical size |
| NumRooms | Integer | Number of rooms | 8 | Treatment rooms |
| MonthlyRent | Decimal | Monthly rent | 280000 | Fixed cost |
| IsActive | Integer | Active status | 1 | 1=Active, 0=Inactive |

**Key Relationships:**
- BranchID → FactBillingDetail.BranchID
- BranchID → FactAppointment.BranchID
- BranchID → FactPatientVisit.BranchID
- BranchID → DimEmployee.BranchID

**KPIs Enabled:**
- Revenue by Branch/Region
- Branch Performance Comparison
- Geographic Analysis
- Branch Profitability (Revenue - Rent - Staff Costs)

---

## 💊 DimService - Medical Service Dimension

**Purpose:** Service analysis and pricing management  
**Grain:** One row per service/procedure

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| ServiceID | Integer | Primary Key | 1 | Unique service ID |
| ServiceCode | String | ICD-10 Code | Z00.0 | International Classification of Diseases |
| ServiceName | String | Service name | ตรวจสุขภาพทั่วไป | Full name (Thai) |
| ICD10Description | String | ICD-10 Description | General medical examination | English description |
| Category | String | Service category | General Medicine | Main category |
| SubCategory | String | Service subcategory | Consultation | Detail category |
| BasePrice | Decimal | Standard price | 500.00 | List price |
| Cost | Decimal | Service cost | 150.00 | Direct cost |
| Duration | Integer | Duration (minutes) | 30 | Service time |

**Note:** ICD-10 codes are used for diagnosis coding. Z-codes (Z00-Z99) are used for health services and preventive care.

**Service Categories:**
- General Medicine
- Dermatology
- Dental
- Orthopedics
- Laboratory
- Vaccination
- Health Package

**ICD-10 Code Categories Used:**
- **Z00-Z13**: Health services and preventive care (checkups, screening, vaccination)
- **K00-K14**: Diseases of oral cavity (dental conditions)
- **L00-L99**: Diseases of skin and subcutaneous tissue (dermatology)
- **M00-M99**: Diseases of musculoskeletal system (orthopedics)
- **R00-R99**: Symptoms, signs and abnormal findings (general symptoms)

**Key Relationships:**
- ServiceID → FactBillingDetail.ServiceID
- ServiceID → FactAppointment.ServiceID

**KPIs Enabled:**
- Revenue by Service/Category
- Service Profitability Analysis
- Popular Services Ranking
- Service Mix Analysis

---

## 👨‍⚕️ DimDoctor - Doctor Dimension

**Purpose:** Doctor performance and scheduling analysis  
**Grain:** One row per doctor

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| DoctorID | Integer | Primary Key | 1 | Unique doctor ID |
| DoctorCode | String | Doctor code | DR001 | Short code |
| DoctorName | String | Doctor name | นพ.สมชาย ใจดี | Full name with title |
| Specialty | String | Medical specialty | General Medicine | Area of expertise |
| LicenseNumber | String | License number | MD12345 | Medical license |
| YearsOfExperience | Integer | Years of experience | 15 | Work experience |
| EducationLevel | String | Education | MD | Degree/certification |
| HourlyRate | Decimal | Hourly rate | 1500.00 | Cost per hour |
| Status | String | Employment status | Active | Active/Inactive |
| HireDate | Date | Hire date | 2020-01-15 | Start date |

**Key Relationships:**
- DoctorID → FactBillingDetail.DoctorID
- DoctorID → FactAppointment.DoctorID
- DoctorID → FactPatientVisit.DoctorID

**KPIs Enabled:**
- Revenue per Doctor
- Patient Volume per Doctor
- Doctor Utilization Rate
- Average Revenue per Visit by Doctor

---

## 👥 DimEmployee - Employee Dimension

**Purpose:** Staff analysis and HR management  
**Grain:** One row per employee

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| EmployeeID | Integer | Primary Key | 1 | Unique employee ID |
| EmployeeCode | String | Employee code | EMP0001 | Short code |
| EmployeeName | String | Employee name | Nurse 1 สาขา 1 | Full name |
| Position | String | Job position | Nurse | Job title |
| Department | String | Department | Operations | Department name |
| BranchID | Integer | Branch ID | 1 | Foreign key to branch |
| MonthlySalary | Decimal | Monthly salary | 30000.00 | Base salary |
| HireDate | Date | Hire date | 2020-01-15 | Employment start |
| Status | String | Employment status | Active | Active/Inactive |

**Positions:**
- Nurse
- Receptionist
- Admin
- Cleaning

**Key Relationships:**
- BranchID → DimBranch.BranchID

**KPIs Enabled:**
- Staff Costs by Branch
- Employee Headcount Analysis
- Salary Cost Analysis
- Revenue per Employee

---

## 💳 DimPaymentMethod - Payment Method Dimension

**Purpose:** Payment analysis and fee management  
**Grain:** One row per payment method

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| PaymentMethodID | Integer | Primary Key | 1 | Unique payment method ID |
| PaymentMethodCode | String | Payment code | CASH | Short code |
| PaymentMethodName | String | Payment name | เงินสด | Full name |
| Category | String | Payment category | Cash | Category grouping |
| IsActive | Integer | Active status | 1 | 1=Active, 0=Inactive |
| ProcessingFee | Decimal | Fee percentage | 0.00 | Processing fee % |

**Payment Categories:**
- Cash
- Credit Card
- Debit Card
- Bank Transfer
- E-Wallet
- Installment

**Key Relationships:**
- PaymentMethodID → FactBillingDetail.PaymentMethodID

**KPIs Enabled:**
- Payment Mix Analysis
- Payment Fee Impact
- Payment Method Trends

---

## 🏥 DimInsurance - Insurance Company Dimension

**Purpose:** Insurance analysis and coverage tracking  
**Grain:** One row per insurance plan

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| InsuranceID | Integer | Primary Key | 1 | Unique insurance ID |
| InsuranceCode | String | Insurance code | SELF | Short code |
| InsuranceName | String | Insurance name | ไม่มีประกัน (จ่ายเอง) | Full name |
| CompanyName | String | Company name | Self Pay | Insurance company |
| CoveragePercent | Decimal | Coverage % | 0.00 | Coverage percentage |
| IsActive | Integer | Active status | 1 | 1=Active, 0=Inactive |

**Key Relationships:**
- InsuranceID → FactBillingDetail.InsuranceID
- InsuranceID → FactPatientVisit.InsuranceID

**KPIs Enabled:**
- Insurance Coverage Analysis
- Self-Pay vs Insured Ratio
- Revenue by Insurance Type

---

## 🏥 DimPatient - Patient Dimension

**Purpose:** Patient demographic analysis (anonymized)  
**Grain:** One row per patient  
**Note:** Simplified for privacy protection

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| PatientID | Integer | Primary Key | 1 | Unique patient ID |
| PatientCode | String | Patient code | PT000001 | Anonymous code |
| Gender | String | Gender | M | M/F |
| AgeGroup | String | Age range | 31-45 | Age grouping |
| Province | String | Province | กรุงเทพมหานคร | Province of residence |
| MembershipLevel | String | Membership tier | Gold | Loyalty program |
| RegistrationDate | Date | Registration date | 2020-01-15 | First visit date |
| IsActive | Integer | Active status | 1 | 1=Active, 0=Inactive |

**Age Groups:**
- 0-17 (Children)
- 18-30 (Young Adults)
- 31-45 (Adults)
- 46-60 (Middle Age)
- 60+ (Seniors)

**Membership Levels:**
- None (Regular)
- Silver (3+ visits)
- Gold (10+ visits)
- Platinum (20+ visits)

**Key Relationships:**
- PatientID → FactBillingDetail.PatientID
- PatientID → FactAppointment.PatientID
- PatientID → FactPatientVisit.PatientID

**KPIs Enabled:**
- Patient Demographics
- Patient Retention Rate
- Lifetime Value Analysis
- New vs Returning Patients

---

## 📅 FactAppointment - Appointment Fact Table

**Purpose:** Appointment scheduling and no-show analysis  
**Grain:** One row per appointment

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| AppointmentID | Integer | Primary Key | 1 | Unique appointment ID |
| AppointmentDateKey | Integer | Date key | 20250101 | FK to DimDate |
| AppointmentTime | String | Time slot | 09:00 | Appointment time |
| PatientID | Integer | Patient ID | 123 | FK to DimPatient |
| BranchID | Integer | Branch ID | 1 | FK to DimBranch |
| DoctorID | Integer | Doctor ID | 1 | FK to DimDoctor |
| ServiceID | Integer | Service ID | 1 | FK to DimService |
| Status | String | Appointment status | Completed | Status indicator |

**Status Values:**
- Scheduled (นัดหมายแล้ว)
- Completed (มาใช้บริการแล้ว)
- Cancelled (ยกเลิก)
- No-Show (ไม่มา)

**KPIs Enabled:**
- Appointment Volume
- No-Show Rate
- Cancellation Rate
- Appointment Utilization
- Popular Time Slots

---

## 🏥 FactPatientVisit - Patient Visit Fact Table

**Purpose:** Patient flow and satisfaction analysis  
**Grain:** One row per visit

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| VisitID | Integer | Primary Key | 1 | Unique visit ID |
| VisitDateKey | Integer | Date key | 20250101 | FK to DimDate |
| PatientID | Integer | Patient ID | 123 | FK to DimPatient |
| BranchID | Integer | Branch ID | 1 | FK to DimBranch |
| DoctorID | Integer | Doctor ID | 1 | FK to DimDoctor |
| InsuranceID | Integer | Insurance ID | 1 | FK to DimInsurance |
| CheckInTime | String | Check-in time | 09:00 | Arrival time |
| CheckOutTime | String | Check-out time | 10:30 | Departure time |
| WaitingTimeMinutes | Integer | Wait time | 25 | Minutes waited |
| ServiceTimeMinutes | Integer | Service time | 45 | Service duration |
| SatisfactionScore | Integer | Rating | 5 | 1-5 scale |

**KPIs Enabled:**
- Patient Volume
- Average Waiting Time
- Average Service Time
- Patient Satisfaction Score
- Visit Duration Analysis
- Doctor Efficiency

---

## 💰 FactBillingDetail - Billing Detail Fact Table (PRIMARY)

**Purpose:** Core financial and revenue analysis  
**Grain:** One row per billing line item  
**Note:** This is the main fact table for revenue analysis

| Column Name | Data Type | Description | Example | Notes |
|------------|-----------|-------------|---------|-------|
| BillingID | Integer | Primary Key | 1 | Unique billing ID |
| BillingNumber | String | Invoice number | INV20250101-000001 | Invoice reference |
| BillingDateKey | Integer | Date key | 20250101 | FK to DimDate |
| VisitID | Integer | Visit ID | 123 | FK to FactPatientVisit (nullable) |
| PatientID | Integer | Patient ID | 123 | FK to DimPatient |
| BranchID | Integer | Branch ID | 1 | FK to DimBranch |
| DoctorID | Integer | Doctor ID | 1 | FK to DimDoctor |
| ServiceID | Integer | Service ID | 1 | FK to DimService |
| InsuranceID | Integer | Insurance ID | 1 | FK to DimInsurance |
| PaymentMethodID | Integer | Payment method ID | 1 | FK to DimPaymentMethod |
| Quantity | Integer | Quantity | 1 | Number of units |
| UnitPrice | Decimal | Unit price | 500.00 | Price per unit |
| GrossAmount | Decimal | Gross amount | 500.00 | Before discount |
| DiscountPercent | Decimal | Discount % | 10.00 | Discount percentage |
| DiscountAmount | Decimal | Discount amount | 50.00 | Discount in baht |
| NetAmount | Decimal | Net amount | 450.00 | After discount |
| InsuranceCoverageAmount | Decimal | Insurance pays | 360.00 | Insurance coverage |
| PatientPaidAmount | Decimal | Patient pays | 90.00 | Out-of-pocket |
| PaymentFee | Decimal | Processing fee | 2.25 | Transaction fee |
| TotalCost | Decimal | Total cost | 150.00 | Direct cost |
| GrossProfit | Decimal | Gross profit | 297.75 | Net - Cost - Fee |
| GrossProfitMargin | Decimal | Profit margin % | 66.17 | Profit % |
| PaymentStatus | String | Payment status | Paid | Payment state |
| PaymentDate | Date | Payment date | 2025-01-01 | Actual payment date |

**Payment Status Values:**
- Paid (ชำระแล้ว)
- Pending (รอชำระ)
- Cancelled (ยกเลิก)

**Key Financial Formulas:**
```
GrossAmount = UnitPrice × Quantity
DiscountAmount = GrossAmount × (DiscountPercent / 100)
NetAmount = GrossAmount - DiscountAmount
InsuranceCoverageAmount = NetAmount × (InsuranceCoveragePercent / 100)
PatientPaidAmount = NetAmount - InsuranceCoverageAmount
PaymentFee = PatientPaidAmount × (ProcessingFeePercent / 100)
GrossProfit = NetAmount - TotalCost - PaymentFee
GrossProfitMargin = (GrossProfit / NetAmount) × 100
```

**KPIs Enabled:**
- Total Revenue (Net Amount)
- Total Cost
- Gross Profit & Margin
- Revenue by Service/Branch/Doctor
- Average Transaction Value
- Discount Impact
- Insurance vs Self-Pay Analysis
- Payment Method Mix
- Revenue Growth Trends
- Profitability Analysis

---

## 🔗 Recommended Relationships in Power BI

### Star Schema Relationships

```
DimDate (DateKey) ----< FactBillingDetail (BillingDateKey)
DimDate (DateKey) ----< FactAppointment (AppointmentDateKey)
DimDate (DateKey) ----< FactPatientVisit (VisitDateKey)

DimBranch (BranchID) ----< FactBillingDetail (BranchID)
DimBranch (BranchID) ----< FactAppointment (BranchID)
DimBranch (BranchID) ----< FactPatientVisit (BranchID)
DimBranch (BranchID) ----< DimEmployee (BranchID)

DimService (ServiceID) ----< FactBillingDetail (ServiceID)
DimService (ServiceID) ----< FactAppointment (ServiceID)

DimDoctor (DoctorID) ----< FactBillingDetail (DoctorID)
DimDoctor (DoctorID) ----< FactAppointment (DoctorID)
DimDoctor (DoctorID) ----< FactPatientVisit (DoctorID)

DimPatient (PatientID) ----< FactBillingDetail (PatientID)
DimPatient (PatientID) ----< FactAppointment (PatientID)
DimPatient (PatientID) ----< FactPatientVisit (PatientID)

DimInsurance (InsuranceID) ----< FactBillingDetail (InsuranceID)
DimInsurance (InsuranceID) ----< FactPatientVisit (InsuranceID)

DimPaymentMethod (PaymentMethodID) ----< FactBillingDetail (PaymentMethodID)

FactPatientVisit (VisitID) ----< FactBillingDetail (VisitID) [Nullable]
```

**Relationship Type:** One-to-Many (Dimension → Fact)  
**Cardinality:** 1:* (Single Direction)  
**Cross Filter Direction:** Single (from Dimension to Fact)

---

## 📈 Key Measures for Power BI

### Financial Measures

```DAX
Total Revenue = SUM(FactBillingDetail[NetAmount])
Total Cost = SUM(FactBillingDetail[TotalCost])
Gross Profit = SUM(FactBillingDetail[GrossProfit])
Gross Profit Margin = DIVIDE([Gross Profit], [Total Revenue], 0)
Average Transaction Value = AVERAGE(FactBillingDetail[NetAmount])
```

### Volume Measures

```DAX
Total Visits = COUNTROWS(FactPatientVisit)
Total Appointments = COUNTROWS(FactAppointment)
Total Transactions = COUNTROWS(FactBillingDetail)
Unique Patients = DISTINCTCOUNT(FactBillingDetail[PatientID])
```

### Performance Measures

```DAX
No-Show Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(FactAppointment), FactAppointment[Status] = "No-Show"),
    COUNTROWS(FactAppointment),
    0
)

Average Waiting Time = AVERAGE(FactPatientVisit[WaitingTimeMinutes])
Average Satisfaction = AVERAGE(FactPatientVisit[SatisfactionScore])
```

---

## 🎯 Recommended Dashboards

### 1. Executive Dashboard (ผู้บริหาร)
- Total Revenue, Profit, Margin (KPI Cards)
- Revenue Trend (Line Chart)
- Revenue by Branch (Bar Chart)
- Revenue by Service Category (Pie Chart)
- Top 10 Services (Table)

### 2. Branch Performance Dashboard (ประสิทธิภาพสาขา)
- Branch Comparison Matrix
- Revenue vs Target by Branch
- Profitability by Branch
- Patient Volume by Branch
- Branch Utilization Rate

### 3. Financial Dashboard (การเงิน)
- P&L Summary
- Revenue Breakdown (Service/Branch/Region)
- Cost Analysis
- Payment Method Analysis
- Discount Impact Analysis

### 4. HR Dashboard (บริหารบุคลากร)
- Staff Headcount by Branch
- Salary Cost Analysis
- Revenue per Employee
- Doctor Performance (Revenue/Patient Volume)
- Employee Utilization

### 5. Patient Service Dashboard (บริการผู้ป่วย)
- Patient Volume Trends
- Waiting Time Analysis
- Satisfaction Scores
- No-Show Rate
- Patient Demographics

---

## 💡 Tips for Power BI Implementation

1. **Mark Date Table:** Set DimDate as the Date Table in Power BI
2. **Create Hierarchies:** 
   - Date: Year → Quarter → Month → Date
   - Location: Region → Province → Branch
   - Service: Category → SubCategory → Service
3. **Use Calculated Columns Sparingly:** Prefer measures for better performance
4. **Set Data Types Correctly:** Ensure dates are Date type, numbers are Decimal
5. **Create Parameter Tables:** For dynamic measure selection
6. **Use Bookmarks:** For dashboard navigation
7. **Implement Row-Level Security:** If needed for multi-tenant access

---

## 📋 Data Quality Notes

- All dates are in Thai business days (Monday-Sunday)
- Currency is in Thai Baht (THB)
- Patient data is anonymized for privacy
- Mock data covers period: January 2023 - October 2025
- Realistic business distributions applied to data generation
- **ICD-10 codes are used for service classification** (in real practice, procedures may also use ICD-9-CM or CPT codes)

---

## 🔍 About ICD-10 Codes

**What is ICD-10?**  
The International Classification of Diseases, 10th Revision (ICD-10) is a medical classification list by the World Health Organization (WHO). It's primarily used for diagnosis coding.

**ICD-10 Code Structure:**
- **Letter + Numbers**: e.g., Z00.0, L70.0, K02.9
- **Categories in this dataset:**
  - **Z codes (Z00-Z99)**: Factors influencing health status (checkups, vaccination, screening)
  - **K codes (K00-K14)**: Oral cavity diseases (dental)
  - **L codes (L00-L99)**: Skin and subcutaneous tissue diseases (dermatology)
  - **M codes (M00-M99)**: Musculoskeletal diseases (orthopedics)
  - **R codes (R00-R99)**: Symptoms and signs (general)

**Note for Thai Healthcare:**  
In Thailand, medical facilities often use:
- **ICD-10-TM** (Thai Modification) for diagnoses
- **TMT codes** (Thai Medical Tariff) for procedures
- **NHSO codes** for social security reimbursement

This dataset uses standard ICD-10 codes for international compatibility.

---

**Generated by:** Medical Clinic Power BI Data Generator  
**Version:** 1.0  
**Last Updated:** 2025-01-09
