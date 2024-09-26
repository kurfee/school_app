from odoo import models, fields, api
from datetime import date
import base64

class StudentMaster(models.Model):
    _name = 'student.master'
    _description = 'Student Master'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    class_level = fields.Selection([
        ('1st Class', '1st Class'),
        ('2nd Class', '2nd Class'),
        ('3rd Class', '3rd Class'),
        ('4th Class', '4th Class'),
        ('5th Class', '5th Class'),
        ('6th Class', '6th Class'),
        ('7th Class', '7th Class'),
        ('8th Class', '8th Class'),
        ('9th Class', '9th Class'),
        ('10th Class', '10th Class'),
    ], string="Class Level", required=True)

    student_code = fields.Char(string='Student Code', readonly=True, copy=False)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    status = fields.Selection([('draft', 'Select'),
                               ('active', 'Active'),
                               ('inactive', 'Inactive')], string='Status',
                              default='draft')
    image = fields.Image(string='Image', attachment=True)
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Activities')

    @api.model
    def create(self, vals):
        # Generate the sequence for student_code if not provided
        if not vals.get('student_code'):
            vals['student_code'] = self.env['ir.sequence'].next_by_code('student.master') or '/'
        return super(StudentMaster, self).create(vals)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = today.year - rec.date_of_birth.year - (
                            (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0



class SubjectMaster(models.Model):
    _name = 'subject.master'
    _description = 'Subject Master'

    name = fields.Char(string='Subject Name', required=True)
    subject_code = fields.Char(string='Subject Code', required=True, unique=True)
    class_level = fields.Selection([
        ('1', '1st Class'),
        ('2', '2nd Class'),
        ('3', '3rd Class'),
        ('4', '4th Class'),
        ('5', '5th Class'),
        ('6', '6th Class'),
        ('7', '7th Class'),
        ('8', '8th Class'),
        ('9', '9th Class'),
        ('10', '10th Class'),
    ], string="Class Level", required=True)

    # One2many field linking to exam_marks_line
    exam_marks_line_ids = fields.One2many('exam.marks.line', 'subject_id')
    marks = fields.Integer(string='Total Marks', required=True)




