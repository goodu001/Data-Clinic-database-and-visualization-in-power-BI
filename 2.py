import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

print("🏥 Medical Clinic Power BI Mock Data Generator")
print("=" * 60)

# =============================================================================
# 1. DimDate - Date Dimension
# =============================================================================
print("\n📅 Generating DimDate...")
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

dim_date = pd.DataFrame({
    'DateKey': [int(d.strftime('%Y%m%d')) for d in date_range],
    'Date': date_range,
    'Year': [d.year for d in date_range],
    'Quarter': [f'Q{(d.month-1)//3 + 1}' for d in date_range],
    'Month': [d.month for d in date_range],
    'MonthName': [d.strftime('%B') for d in date_range],
    'MonthNameThai': [['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน',
                       'กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'][d.month-1] for d in date_range],
    'Day': [d.day for d in date_range],
    'DayOfWeek': [d.weekday() + 1 for d in date_range],
    'DayName': [d.strftime('%A') for d in date_range],
    'WeekOfYear': [d.isocalendar()[1] for d in date_range],
    'IsWeekend': [1 if d.weekday() >= 5 else 0 for d in date_range],
    'FiscalYear': [d.year if d.month >= 10 else d.year for d in date_range]
})

# =============================================================================
# 2. DimBranch - Branch/Clinic Dimension
# =============================================================================
print("🏢 Generating DimBranch...")
branches = [
    {'BranchID': 1, 'BranchCode': 'BKK-CTW', 'BranchName': 'คลินิกเซ็นทรัลเวิลด์', 'Region': 'กรุงเทพฯ', 
     'Province': 'กรุงเทพมหานคร', 'District': 'ปทุมวัน', 'Size': 'Large', 'OpenDate': '2020-01-15', 
     'SquareMeter': 450, 'NumRooms': 8, 'MonthlyRent': 280000, 'IsActive': 1},
    {'BranchID': 2, 'BranchCode': 'BKK-SKM', 'BranchName': 'คลินิกสุขุมวิท', 'Region': 'กรุงเทพฯ', 
     'Province': 'กรุงเทพมหานคร', 'District': 'วัฒนา', 'Size': 'Large', 'OpenDate': '2020-06-01', 
     'SquareMeter': 380, 'NumRooms': 7, 'MonthlyRent': 250000, 'IsActive': 1},
    {'BranchID': 3, 'BranchCode': 'BKK-STW', 'BranchName': 'คลินิกสาทร', 'Region': 'กรุงเทพฯ', 
     'Province': 'กรุงเทพมหานคร', 'District': 'สาทร', 'Size': 'Medium', 'OpenDate': '2021-03-20', 
     'SquareMeter': 280, 'NumRooms': 5, 'MonthlyRent': 180000, 'IsActive': 1},
    {'BranchID': 4, 'BranchCode': 'CMI-NMM', 'BranchName': 'คลินิกนิมมาน', 'Region': 'ภาคเหนือ', 
     'Province': 'เชียงใหม่', 'District': 'เมือง', 'Size': 'Medium', 'OpenDate': '2021-08-15', 
     'SquareMeter': 300, 'NumRooms': 6, 'MonthlyRent': 120000, 'IsActive': 1},
    {'BranchID': 5, 'BranchCode': 'PKT-PTL', 'BranchName': 'คลินิกภูเก็ต', 'Region': 'ภาคใต้', 
     'Province': 'ภูเก็ต', 'District': 'กะทู้', 'Size': 'Medium', 'OpenDate': '2022-01-10', 
     'SquareMeter': 320, 'NumRooms': 6, 'MonthlyRent': 140000, 'IsActive': 1},
    {'BranchID': 6, 'BranchCode': 'HDY-CTR', 'BranchName': 'คลินิกหาดใหญ่', 'Region': 'ภาคใต้', 
     'Province': 'สงขลา', 'District': 'หาดใหญ่', 'Size': 'Small', 'OpenDate': '2022-09-01', 
     'SquareMeter': 200, 'NumRooms': 4, 'MonthlyRent': 70000, 'IsActive': 1},
    {'BranchID': 7, 'BranchCode': 'KKN-CTR', 'BranchName': 'คลินิกขอนแก่น', 'Region': 'ภาคอีสาน', 
     'Province': 'ขอนแก่น', 'District': 'เมือง', 'Size': 'Medium', 'OpenDate': '2023-02-15', 
     'SquareMeter': 260, 'NumRooms': 5, 'MonthlyRent': 85000, 'IsActive': 1},
    {'BranchID': 8, 'BranchCode': 'CHB-CTR', 'BranchName': 'คลินิกชลบุรี', 'Region': 'ภาคตะวันออก', 
     'Province': 'ชลบุรี', 'District': 'เมือง', 'Size': 'Small', 'OpenDate': '2023-07-01', 
     'SquareMeter': 220, 'NumRooms': 4, 'MonthlyRent': 75000, 'IsActive': 1},
]
dim_branch = pd.DataFrame(branches)

# =============================================================================
# 3. DimService - Medical Service Dimension
# =============================================================================
print("💊 Generating DimService...")
services = [
    # General Medicine
    {'ServiceID': 1, 'ServiceCode': 'Z00.0', 'ServiceName': 'ตรวจสุขภาพทั่วไป', 
     'ICD10Description': 'General medical examination', 
     'Category': 'General Medicine', 'SubCategory': 'Consultation', 'BasePrice': 500, 'Cost': 150, 'Duration': 30},
    {'ServiceID': 2, 'ServiceCode': 'R50.9', 'ServiceName': 'ตรวจรักษาโรคทั่วไป', 
     'ICD10Description': 'Fever, unspecified', 
     'Category': 'General Medicine', 'SubCategory': 'Treatment', 'BasePrice': 800, 'Cost': 250, 'Duration': 45},
    
    # Dermatology
    {'ServiceID': 3, 'ServiceCode': 'L98.9', 'ServiceName': 'ตรวจผิวหนัง', 
     'ICD10Description': 'Disorder of skin and subcutaneous tissue', 
     'Category': 'Dermatology', 'SubCategory': 'Consultation', 'BasePrice': 1000, 'Cost': 300, 'Duration': 30},
    {'ServiceID': 4, 'ServiceCode': 'L70.0', 'ServiceName': 'รักษาสิว', 
     'ICD10Description': 'Acne vulgaris', 
     'Category': 'Dermatology', 'SubCategory': 'Treatment', 'BasePrice': 2500, 'Cost': 800, 'Duration': 60},
    {'ServiceID': 5, 'ServiceCode': 'L81.9', 'ServiceName': 'เลเซอร์หน้าใส', 
     'ICD10Description': 'Disorder of pigmentation', 
     'Category': 'Dermatology', 'SubCategory': 'Aesthetic', 'BasePrice': 5000, 'Cost': 1500, 'Duration': 90},
    
    # Dental
    {'ServiceID': 6, 'ServiceCode': 'Z01.2', 'ServiceName': 'ตรวจฟัน', 
     'ICD10Description': 'Dental examination', 
     'Category': 'Dental', 'SubCategory': 'Consultation', 'BasePrice': 300, 'Cost': 100, 'Duration': 30},
    {'ServiceID': 7, 'ServiceCode': 'K02.9', 'ServiceName': 'อุดฟัน', 
     'ICD10Description': 'Dental caries', 
     'Category': 'Dental', 'SubCategory': 'Treatment', 'BasePrice': 1500, 'Cost': 500, 'Duration': 60},
    {'ServiceID': 8, 'ServiceCode': 'K03.6', 'ServiceName': 'ขูดหินปูน', 
     'ICD10Description': 'Deposits on teeth', 
     'Category': 'Dental', 'SubCategory': 'Treatment', 'BasePrice': 1200, 'Cost': 400, 'Duration': 45},
    {'ServiceID': 9, 'ServiceCode': 'K03.7', 'ServiceName': 'ฟอกสีฟัน', 
     'ICD10Description': 'Posteruptive color changes of dental hard tissues', 
     'Category': 'Dental', 'SubCategory': 'Aesthetic', 'BasePrice': 8000, 'Cost': 2500, 'Duration': 120},
    
    # Orthopedics
    {'ServiceID': 10, 'ServiceCode': 'M25.9', 'ServiceName': 'ตรวจกระดูกและข้อ', 
     'ICD10Description': 'Joint disorder, unspecified', 
     'Category': 'Orthopedics', 'SubCategory': 'Consultation', 'BasePrice': 1200, 'Cost': 350, 'Duration': 30},
    {'ServiceID': 11, 'ServiceCode': 'M79.3', 'ServiceName': 'กายภาพบำบัด', 
     'ICD10Description': 'Panniculitis, unspecified (for physiotherapy)', 
     'Category': 'Orthopedics', 'SubCategory': 'Treatment', 'BasePrice': 1800, 'Cost': 600, 'Duration': 60},
    
    # Lab Tests
    {'ServiceID': 12, 'ServiceCode': 'Z00.00', 'ServiceName': 'เจาะเลือดตรวจสุขภาพ', 
     'ICD10Description': 'General medical examination without complaint', 
     'Category': 'Laboratory', 'SubCategory': 'Blood Test', 'BasePrice': 1500, 'Cost': 400, 'Duration': 15},
    {'ServiceID': 13, 'ServiceCode': 'R82.90', 'ServiceName': 'ตรวจปัสสาวะ', 
     'ICD10Description': 'Unspecified abnormal findings in urine', 
     'Category': 'Laboratory', 'SubCategory': 'Urine Test', 'BasePrice': 300, 'Cost': 80, 'Duration': 10},
    {'ServiceID': 14, 'ServiceCode': 'Z01.6', 'ServiceName': 'X-Ray', 
     'ICD10Description': 'Radiological examination', 
     'Category': 'Laboratory', 'SubCategory': 'Imaging', 'BasePrice': 800, 'Cost': 250, 'Duration': 20},
    
    # Vaccination
    {'ServiceID': 15, 'ServiceCode': 'Z25.1', 'ServiceName': 'วัคซีนไข้หวัดใหญ่', 
     'ICD10Description': 'Need for immunization against influenza', 
     'Category': 'Vaccination', 'SubCategory': 'Flu', 'BasePrice': 600, 'Cost': 350, 'Duration': 15},
    {'ServiceID': 16, 'ServiceCode': 'Z28.3', 'ServiceName': 'วัคซีนโควิด-19', 
     'ICD10Description': 'Underimmunization status (COVID-19)', 
     'Category': 'Vaccination', 'SubCategory': 'COVID-19', 'BasePrice': 0, 'Cost': 0, 'Duration': 15},
    
    # Health Checkup Packages
    {'ServiceID': 17, 'ServiceCode': 'Z00.01', 'ServiceName': 'แพ็คเกจตรวจสุขภาพพื้นฐาน', 
     'ICD10Description': 'General medical examination with abnormal findings', 
     'Category': 'Health Package', 'SubCategory': 'Basic', 'BasePrice': 3500, 'Cost': 1200, 'Duration': 90},
    {'ServiceID': 18, 'ServiceCode': 'Z13.9', 'ServiceName': 'แพ็คเกจตรวจสุขภาพแบบครอบคลุม', 
     'ICD10Description': 'Special screening examination, unspecified', 
     'Category': 'Health Package', 'SubCategory': 'Comprehensive', 'BasePrice': 8500, 'Cost': 3000, 'Duration': 180},
]
dim_service = pd.DataFrame(services)

# =============================================================================
# 4. DimDoctor - Doctor Dimension
# =============================================================================
print("👨‍⚕️ Generating DimDoctor...")
doctors = [
    {'DoctorID': 1, 'DoctorCode': 'DR001', 'DoctorName': 'นพ.สมชาย ใจดี', 'Specialty': 'General Medicine', 
     'LicenseNumber': 'MD12345', 'YearsOfExperience': 15, 'EducationLevel': 'MD', 'HourlyRate': 1500, 
     'Status': 'Active', 'HireDate': '2020-01-15'},
    {'DoctorID': 2, 'DoctorCode': 'DR002', 'DoctorName': 'นพ.วิชัย รักษา', 'Specialty': 'Dermatology', 
     'LicenseNumber': 'MD12346', 'YearsOfExperience': 12, 'EducationLevel': 'MD, Board Certified', 'HourlyRate': 2000, 
     'Status': 'Active', 'HireDate': '2020-02-01'},
    {'DoctorID': 3, 'DoctorCode': 'DR003', 'DoctorName': 'ทพญ.สุดา สวยงาม', 'Specialty': 'Dermatology', 
     'LicenseNumber': 'MD12347', 'YearsOfExperience': 10, 'EducationLevel': 'MD, Board Certified', 'HourlyRate': 2000, 
     'Status': 'Active', 'HireDate': '2020-03-15'},
    {'DoctorID': 4, 'DoctorCode': 'DR004', 'DoctorName': 'ทพ.ชัยวัฒน์ ยิ้มแย้ม', 'Specialty': 'Dental', 
     'LicenseNumber': 'DT12348', 'YearsOfExperience': 8, 'EducationLevel': 'DDS', 'HourlyRate': 1800, 
     'Status': 'Active', 'HireDate': '2020-06-01'},
    {'DoctorID': 5, 'DoctorCode': 'DR005', 'DoctorName': 'ทพญ.มาลี รอยยิ้ม', 'Specialty': 'Dental', 
     'LicenseNumber': 'DT12349', 'YearsOfExperience': 6, 'EducationLevel': 'DDS', 'HourlyRate': 1600, 
     'Status': 'Active', 'HireDate': '2021-01-15'},
    {'DoctorID': 6, 'DoctorCode': 'DR006', 'DoctorName': 'นพ.ประเสริฐ แข็งแรง', 'Specialty': 'Orthopedics', 
     'LicenseNumber': 'MD12350', 'YearsOfExperience': 14, 'EducationLevel': 'MD, Board Certified', 'HourlyRate': 2200, 
     'Status': 'Active', 'HireDate': '2021-03-01'},
    {'DoctorID': 7, 'DoctorCode': 'DR007', 'DoctorName': 'นพ.อนุชา เจริญ', 'Specialty': 'General Medicine', 
     'LicenseNumber': 'MD12351', 'YearsOfExperience': 9, 'EducationLevel': 'MD', 'HourlyRate': 1400, 
     'Status': 'Active', 'HireDate': '2021-08-01'},
    {'DoctorID': 8, 'DoctorCode': 'DR008', 'DoctorName': 'ทพญ.ศิริพร สุขสม', 'Specialty': 'General Medicine', 
     'LicenseNumber': 'MD12352', 'YearsOfExperience': 7, 'EducationLevel': 'MD', 'HourlyRate': 1300, 
     'Status': 'Active', 'HireDate': '2022-01-15'},
    {'DoctorID': 9, 'DoctorCode': 'DR009', 'DoctorName': 'ทพ.สมศักดิ์ สุดหล่อ', 'Specialty': 'Dental', 
     'LicenseNumber': 'DT12353', 'YearsOfExperience': 5, 'EducationLevel': 'DDS', 'HourlyRate': 1500, 
     'Status': 'Active', 'HireDate': '2022-09-01'},
    {'DoctorID': 10, 'DoctorCode': 'DR010', 'DoctorName': 'นพ.ธนา มั่งมี', 'Specialty': 'Dermatology', 
     'LicenseNumber': 'MD12354', 'YearsOfExperience': 11, 'EducationLevel': 'MD, Board Certified', 'HourlyRate': 2100, 
     'Status': 'Active', 'HireDate': '2023-02-01'},
]
dim_doctor = pd.DataFrame(doctors)

# =============================================================================
# 5. DimEmployee - Employee Dimension
# =============================================================================
print("👥 Generating DimEmployee...")
employees = []
emp_id = 1

# Generate employees for each branch
for branch_id in range(1, 9):
    branch_size = dim_branch[dim_branch['BranchID'] == branch_id]['Size'].values[0]
    
    # Determine number of employees based on branch size
    if branch_size == 'Large':
        staff_count = {'Nurse': 6, 'Receptionist': 3, 'Admin': 2, 'Cleaning': 2}
    elif branch_size == 'Medium':
        staff_count = {'Nurse': 4, 'Receptionist': 2, 'Admin': 1, 'Cleaning': 1}
    else:  # Small
        staff_count = {'Nurse': 2, 'Receptionist': 1, 'Admin': 1, 'Cleaning': 1}
    
    for position, count in staff_count.items():
        for i in range(count):
            salary_range = {
                'Nurse': (25000, 35000),
                'Receptionist': (18000, 25000),
                'Admin': (22000, 30000),
                'Cleaning': (12000, 15000)
            }
            
            employees.append({
                'EmployeeID': emp_id,
                'EmployeeCode': f'EMP{emp_id:04d}',
                'EmployeeName': f'{position} {i+1} สาขา {branch_id}',
                'Position': position,
                'Department': 'Operations' if position in ['Nurse', 'Receptionist'] else 'Support',
                'BranchID': branch_id,
                'MonthlySalary': random.randint(salary_range[position][0], salary_range[position][1]),
                'HireDate': (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1200))).strftime('%Y-%m-%d'),
                'Status': 'Active'
            })
            emp_id += 1

dim_employee = pd.DataFrame(employees)

# =============================================================================
# 6. DimPaymentMethod - Payment Method Dimension
# =============================================================================
print("💳 Generating DimPaymentMethod...")
payment_methods = [
    {'PaymentMethodID': 1, 'PaymentMethodCode': 'CASH', 'PaymentMethodName': 'เงินสด', 
     'Category': 'Cash', 'IsActive': 1, 'ProcessingFee': 0},
    {'PaymentMethodID': 2, 'PaymentMethodCode': 'CC-VISA', 'PaymentMethodName': 'บัตรเครดิต Visa', 
     'Category': 'Credit Card', 'IsActive': 1, 'ProcessingFee': 2.5},
    {'PaymentMethodID': 3, 'PaymentMethodCode': 'CC-MC', 'PaymentMethodName': 'บัตรเครดิต MasterCard', 
     'Category': 'Credit Card', 'IsActive': 1, 'ProcessingFee': 2.5},
    {'PaymentMethodID': 4, 'PaymentMethodCode': 'DEBIT', 'PaymentMethodName': 'บัตรเดบิต', 
     'Category': 'Debit Card', 'IsActive': 1, 'ProcessingFee': 1.5},
    {'PaymentMethodID': 5, 'PaymentMethodCode': 'BANK-TRF', 'PaymentMethodName': 'โอนเงินผ่านธนาคาร', 
     'Category': 'Bank Transfer', 'IsActive': 1, 'ProcessingFee': 0},
    {'PaymentMethodID': 6, 'PaymentMethodCode': 'PROMPTPAY', 'PaymentMethodName': 'พร้อมเพย์', 
     'Category': 'E-Wallet', 'IsActive': 1, 'ProcessingFee': 0},
    {'PaymentMethodID': 7, 'PaymentMethodCode': 'TRUEMONEY', 'PaymentMethodName': 'ทรูมันนี่วอลเล็ท', 
     'Category': 'E-Wallet', 'IsActive': 1, 'ProcessingFee': 1.0},
    {'PaymentMethodID': 8, 'PaymentMethodCode': 'INSTALLMENT', 'PaymentMethodName': 'ผ่อนชำระ 0%', 
     'Category': 'Installment', 'IsActive': 1, 'ProcessingFee': 3.5},
]
dim_payment_method = pd.DataFrame(payment_methods)

# =============================================================================
# 7. DimInsurance - Insurance Company Dimension
# =============================================================================
print("🏥 Generating DimInsurance...")
insurances = [
    {'InsuranceID': 1, 'InsuranceCode': 'SELF', 'InsuranceName': 'ไม่มีประกัน (จ่ายเอง)', 
     'CompanyName': 'Self Pay', 'CoveragePercent': 0, 'IsActive': 1},
    {'InsuranceID': 2, 'InsuranceCode': 'SSO', 'InsuranceName': 'ประกันสังคม', 
     'CompanyName': 'Social Security Office', 'CoveragePercent': 100, 'IsActive': 1},
    {'InsuranceID': 3, 'InsuranceCode': 'AIA-001', 'InsuranceName': 'AIA Health Plus', 
     'CompanyName': 'AIA Thailand', 'CoveragePercent': 80, 'IsActive': 1},
    {'InsuranceID': 4, 'InsuranceCode': 'ALLIANZ-001', 'InsuranceName': 'Allianz SmartHealth', 
     'CompanyName': 'Allianz Ayudhya', 'CoveragePercent': 90, 'IsActive': 1},
    {'InsuranceID': 5, 'InsuranceCode': 'BUPA-001', 'InsuranceName': 'Bupa Premium', 
     'CompanyName': 'Bupa Thailand', 'CoveragePercent': 100, 'IsActive': 1},
    {'InsuranceID': 6, 'InsuranceCode': 'DHIPAYA-001', 'InsuranceName': 'ธนชาต ประกันสุขภาพ', 
     'CompanyName': 'Dhipaya Insurance', 'CoveragePercent': 70, 'IsActive': 1},
]
dim_insurance = pd.DataFrame(insurances)

# =============================================================================
# 8. DimPatient - Patient Dimension (Simplified for privacy)
# =============================================================================
print("🏥 Generating DimPatient...")
num_patients = 3000

dim_patient = pd.DataFrame({
    'PatientID': range(1, num_patients + 1),
    'PatientCode': [f'PT{i:06d}' for i in range(1, num_patients + 1)],
    'Gender': np.random.choice(['M', 'F'], num_patients, p=[0.45, 0.55]),
    'AgeGroup': np.random.choice(['0-17', '18-30', '31-45', '46-60', '60+'], num_patients, 
                                 p=[0.05, 0.25, 0.35, 0.25, 0.10]),
    'Province': np.random.choice(['กรุงเทพมหานคร', 'เชียงใหม่', 'ภูเก็ต', 'สงขลา', 'ขอนแก่น', 'ชลบุรี', 'อื่นๆ'], 
                                num_patients, p=[0.40, 0.10, 0.08, 0.08, 0.10, 0.12, 0.12]),
    'MembershipLevel': np.random.choice(['None', 'Silver', 'Gold', 'Platinum'], num_patients, 
                                       p=[0.60, 0.20, 0.15, 0.05]),
    'RegistrationDate': [(datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1800))).strftime('%Y-%m-%d') 
                        for _ in range(num_patients)],
    'IsActive': 1
})

# =============================================================================
# 9. FactAppointment - Appointment Fact Table
# =============================================================================
print("📅 Generating FactAppointment...")
num_appointments = 15000

fact_appointment = pd.DataFrame({
    'AppointmentID': range(1, num_appointments + 1),
    'AppointmentDateKey': [int((datetime(2023, 1, 1) + timedelta(days=random.randint(0, 1000))).strftime('%Y%m%d')) 
                          for _ in range(num_appointments)],
    'AppointmentTime': [f'{random.randint(8, 17):02d}:{random.choice([0, 30]):02d}' for _ in range(num_appointments)],
    'PatientID': np.random.randint(1, num_patients + 1, num_appointments),
    'BranchID': np.random.choice(range(1, 9), num_appointments, 
                                p=[0.20, 0.18, 0.15, 0.12, 0.11, 0.09, 0.08, 0.07]),
    'DoctorID': np.random.randint(1, 11, num_appointments),
    'ServiceID': np.random.choice(range(1, 19), num_appointments),
    'Status': np.random.choice(['Scheduled', 'Completed', 'Cancelled', 'No-Show'], num_appointments, 
                              p=[0.15, 0.70, 0.10, 0.05]),
})

# =============================================================================
# 10. FactPatientVisit - Patient Visit Fact Table
# =============================================================================
print("🏥 Generating FactPatientVisit...")
num_visits = 12000

fact_visit = pd.DataFrame({
    'VisitID': range(1, num_visits + 1),
    'VisitDateKey': [int((datetime(2023, 1, 1) + timedelta(days=random.randint(0, 1000))).strftime('%Y%m%d')) 
                    for _ in range(num_visits)],
    'PatientID': np.random.randint(1, num_patients + 1, num_visits),
    'BranchID': np.random.choice(range(1, 9), num_visits, 
                                p=[0.20, 0.18, 0.15, 0.12, 0.11, 0.09, 0.08, 0.07]),
    'DoctorID': np.random.randint(1, 11, num_visits),
    'InsuranceID': np.random.choice(range(1, 7), num_visits, p=[0.45, 0.15, 0.15, 0.10, 0.08, 0.07]),
    'CheckInTime': [f'{random.randint(8, 17):02d}:{random.randint(0, 59):02d}' for _ in range(num_visits)],
    'CheckOutTime': [f'{random.randint(9, 18):02d}:{random.randint(0, 59):02d}' for _ in range(num_visits)],
    'WaitingTimeMinutes': np.random.randint(5, 120, num_visits),
    'ServiceTimeMinutes': np.random.randint(15, 180, num_visits),
    'SatisfactionScore': np.random.choice([1, 2, 3, 4, 5], num_visits, p=[0.02, 0.05, 0.13, 0.35, 0.45]),
})

# =============================================================================
# 11. FactBillingDetail - Billing Detail Fact Table (MAIN FACT TABLE)
# =============================================================================
print("💰 Generating FactBillingDetail...")
num_billing_records = 18000

# Generate billing records
billing_data = []
for i in range(1, num_billing_records + 1):
    visit_id = random.randint(1, num_visits) if random.random() < 0.65 else None
    date_key = int((datetime(2023, 1, 1) + timedelta(days=random.randint(0, 1000))).strftime('%Y%m%d'))
    patient_id = np.random.randint(1, num_patients + 1)
    branch_id = np.random.choice(range(1, 9), p=[0.20, 0.18, 0.15, 0.12, 0.11, 0.09, 0.08, 0.07])
    doctor_id = np.random.randint(1, 11)
    service_id = np.random.choice(range(1, 19))
    insurance_id = np.random.choice(range(1, 7), p=[0.45, 0.15, 0.15, 0.10, 0.08, 0.07])
    payment_method_id = np.random.choice(range(1, 9), p=[0.15, 0.25, 0.20, 0.10, 0.08, 0.12, 0.05, 0.05])
    
    # Get service details
    service = dim_service[dim_service['ServiceID'] == service_id].iloc[0]
    base_price = service['BasePrice']
    cost = service['Cost']
    
    # Calculate quantity and prices
    quantity = random.randint(1, 3) if service['Category'] not in ['Health Package'] else 1
    unit_price = base_price * random.uniform(0.9, 1.1)  # Add some price variation
    discount_percent = random.choice([0, 0, 0, 5, 10, 15, 20]) if random.random() < 0.3 else 0
    
    gross_amount = unit_price * quantity
    discount_amount = gross_amount * (discount_percent / 100)
    net_amount = gross_amount - discount_amount
    
    # Insurance coverage
    insurance = dim_insurance[dim_insurance['InsuranceID'] == insurance_id].iloc[0]
    insurance_coverage_amount = net_amount * (insurance['CoveragePercent'] / 100)
    patient_paid_amount = net_amount - insurance_coverage_amount
    
    # Payment processing fee
    payment = dim_payment_method[dim_payment_method['PaymentMethodID'] == payment_method_id].iloc[0]
    payment_fee = patient_paid_amount * (payment['ProcessingFee'] / 100)
    
    # Total cost
    total_cost = cost * quantity
    gross_profit = net_amount - total_cost - payment_fee
    gross_profit_margin = (gross_profit / net_amount * 100) if net_amount > 0 else 0
    
    billing_data.append({
        'BillingID': i,
        'BillingNumber': f'INV{date_key}-{i:06d}',
        'BillingDateKey': date_key,
        'VisitID': visit_id,
        'PatientID': patient_id,
        'BranchID': branch_id,
        'DoctorID': doctor_id,
        'ServiceID': service_id,
        'InsuranceID': insurance_id,
        'PaymentMethodID': payment_method_id,
        'Quantity': quantity,
        'UnitPrice': round(unit_price, 2),
        'GrossAmount': round(gross_amount, 2),
        'DiscountPercent': discount_percent,
        'DiscountAmount': round(discount_amount, 2),
        'NetAmount': round(net_amount, 2),
        'InsuranceCoverageAmount': round(insurance_coverage_amount, 2),
        'PatientPaidAmount': round(patient_paid_amount, 2),
        'PaymentFee': round(payment_fee, 2),
        'TotalCost': round(total_cost, 2),
        'GrossProfit': round(gross_profit, 2),
        'GrossProfitMargin': round(gross_profit_margin, 2),
        'PaymentStatus': np.random.choice(['Paid', 'Pending', 'Cancelled'], p=[0.92, 0.05, 0.03]),
        'PaymentDate': (datetime.strptime(str(date_key), '%Y%m%d') + 
                       timedelta(days=random.randint(0, 7))).strftime('%Y-%m-%d'),
    })

fact_billing = pd.DataFrame(billing_data)

# =============================================================================
# Save all tables to CSV
# =============================================================================
print("\n💾 Saving all tables to CSV files...")

dim_date.to_csv('DimDate.csv', index=False, encoding='utf-8-sig')
dim_branch.to_csv('DimBranch.csv', index=False, encoding='utf-8-sig')
dim_service.to_csv('DimService.csv', index=False, encoding='utf-8-sig')
dim_doctor.to_csv('DimDoctor.csv', index=False, encoding='utf-8-sig')
dim_employee.to_csv('DimEmployee.csv', index=False, encoding='utf-8-sig')
dim_payment_method.to_csv('DimPaymentMethod.csv', index=False, encoding='utf-8-sig')
dim_insurance.to_csv('DimInsurance.csv', index=False, encoding='utf-8-sig')
dim_patient.to_csv('DimPatient.csv', index=False, encoding='utf-8-sig')
fact_appointment.to_csv('FactAppointment.csv', index=False, encoding='utf-8-sig')
fact_visit.to_csv('FactPatientVisit.csv', index=False, encoding='utf-8-sig')
fact_billing.to_csv('FactBillingDetail.csv', index=False, encoding='utf-8-sig')

print("\n✅ All CSV files generated successfully!")
print(f"\n📊 Summary:")
print(f"   - DimDate: {len(dim_date):,} records")
print(f"   - DimBranch: {len(dim_branch):,} records")
print(f"   - DimService: {len(dim_service):,} records")
print(f"   - DimDoctor: {len(dim_doctor):,} records")
print(f"   - DimEmployee: {len(dim_employee):,} records")
print(f"   - DimPaymentMethod: {len(dim_payment_method):,} records")
print(f"   - DimInsurance: {len(dim_insurance):,} records")
print(f"   - DimPatient: {len(dim_patient):,} records")
print(f"   - FactAppointment: {len(fact_appointment):,} records")
print(f"   - FactPatientVisit: {len(fact_visit):,} records")
print(f"   - FactBillingDetail: {len(fact_billing):,} records")

# =============================================================================
# Generate Data Dictionary
# =============================================================================
print("\n📖 Generating Data Dictionary...")

data_dictionary = """# 📚 Medical Clinic Power BI - Data Dictionary

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
"""

# Save Data Dictionary
with open('DataDictionary.md', 'w', encoding='utf-8') as f:
    f.write(data_dictionary)

print("\n📖 Data Dictionary saved as: DataDictionary.md")

print("\n" + "="*60)
print("🎉 ALL FILES GENERATED SUCCESSFULLY!")
print("="*60)
print("\n📦 Generated Files:")
print("   ✓ 11 CSV files (8 Dimensions + 3 Facts)")
print("   ✓ 1 Data Dictionary (Markdown)")
print("\n🏥 Key Features:")
print("   ✓ ICD-10 codes used for service classification")
print("   ✓ 3 years of realistic medical clinic data (2023-2025)")
print("   ✓ 8 branches across 4 regions in Thailand")
print("   ✓ 18,000 billing transactions with full financial details")
print("\n📂 Next Steps:")
print("   1. Open Power BI Desktop")
print("   2. Get Data → Text/CSV → Import all CSV files")
print("   3. Go to Model View → Create relationships as per Data Dictionary")
print("   4. Mark DimDate as Date Table")
print("   5. Start building your dashboards!")
print("\n💡 Tip: Refer to DataDictionary.md for:")
print("   - Table structures and relationships")
print("   - Recommended measures and KPIs")
print("   - Dashboard ideas")
print("\n🚀 Happy analyzing!")
print("="*60)