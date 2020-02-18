# Generated by Django 2.2.10 on 2020-02-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexible_filter_conditions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='negate',
            field=models.BooleanField(default=False, verbose_name='Negate'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='operation',
            field=models.CharField(choices=[('and', 'and'), ('or', 'or'), ('xor', 'xor')], max_length=30, verbose_name='Operation'),
        ),
        migrations.AlterField(
            model_name='terminalcondition',
            name='operation',
            field=models.CharField(choices=[('=', '='), ('!=', '≠'), ('>', '>'), ('<', '<'), ('>=', '≥'), ('<=', '≤'), ('containts', 'contains'), ('icontaints', 'contains (case insensitive)'), ('isnull', 'variable is null (true or false)'), ('in', 'in list variable type (e.g. list.3,44)')], max_length=30, verbose_name='Operation'),
        ),
        migrations.AlterField(
            model_name='terminalcondition',
            name='value',
            field=models.CharField(blank=True, help_text='Value or variable on right-hand side. <br/>\naction: daily, new-user<br/>\nDateField: month_ago, one_day, one_week, two_weeks, one_month, datetime.2010-01-01 00:00, date.2010-01-01, list.3,5<br/>\nBooleanField: True, False<br/>\nfor blank value: None or Blank', max_length=50, null=True, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='terminalcondition',
            name='variable',
            field=models.CharField(blank=True, choices=[('action', "Action: CharField ('daily', 'new-user', 'new-payment')"), ('User', [('User.id', 'id: AutoField '), ('User.password', 'password: CharField '), ('User.last_login', 'last_login: DateTimeField '), ('User.is_superuser', 'is_superuser: BooleanField '), ('User.username', 'username: CharField '), ('User.first_name', 'first_name: CharField '), ('User.last_name', 'last_name: CharField '), ('User.email', 'email: CharField '), ('User.is_staff', 'is_staff: BooleanField '), ('User.is_active', 'is_active: BooleanField '), ('User.date_joined', 'date_joined: DateTimeField ')]), ('Profile', [('Profile.id', 'id: AutoField '), ('Profile.polymorphic_ctype', 'polymorphic_ctype: ForeignKey '), ('Profile.last_login', 'last_login: DateTimeField '), ('Profile.is_superuser', 'is_superuser: BooleanField '), ('Profile.is_staff', 'is_staff: BooleanField '), ('Profile.is_active', 'is_active: BooleanField '), ('Profile.date_joined', 'date_joined: DateTimeField '), ('Profile.username', 'username: CharField '), ('Profile.password', 'password: CharField '), ('Profile.email', 'email: CharField '), ('Profile.addressment', 'addressment: CharField '), ('Profile.addressment_on_envelope', 'addressment_on_envelope: CharField '), ('Profile.language', "language: CharField ('cs', 'en')"), ('Profile.street', 'street: CharField '), ('Profile.city', 'city: CharField '), ('Profile.country', 'country: CharField '), ('Profile.zip_code', 'zip_code: CharField '), ('Profile.different_correspondence_address', 'different_correspondence_address: BooleanField '), ('Profile.correspondence_street', 'correspondence_street: CharField '), ('Profile.correspondence_city', 'correspondence_city: CharField '), ('Profile.correspondence_country', 'correspondence_country: CharField '), ('Profile.correspondence_zip_code', 'correspondence_zip_code: CharField '), ('Profile.other_support', 'other_support: TextField '), ('Profile.profile_text', 'profile_text: TextField '), ('Profile.profile_picture', 'profile_picture: FileField '), ('Profile.club_card_available', 'club_card_available: BooleanField '), ('Profile.club_card_dispatched', 'club_card_dispatched: BooleanField '), ('Profile.other_benefits', 'other_benefits: TextField '), ('Profile.note', 'note: TextField '), ('Profile.created', 'created: DateTimeField '), ('Profile.updated', 'updated: DateTimeField ')]), ('User.userchannels.payment', [('User.userchannels.payment.id', 'id: AutoField '), ('User.userchannels.payment.date', 'date: DateField '), ('User.userchannels.payment.amount', 'amount: PositiveIntegerField '), ('User.userchannels.payment.account', 'account: CharField '), ('User.userchannels.payment.bank_code', 'bank_code: CharField '), ('User.userchannels.payment.VS', 'VS: CharField '), ('User.userchannels.payment.VS2', 'VS2: CharField '), ('User.userchannels.payment.SS', 'SS: CharField '), ('User.userchannels.payment.KS', 'KS: CharField '), ('User.userchannels.payment.BIC', 'BIC: CharField '), ('User.userchannels.payment.user_identification', 'user_identification: CharField '), ('User.userchannels.payment.type', "type: CharField ('bank-transfer', 'cash', 'expected', 'darujme')"), ('User.userchannels.payment.done_by', 'done_by: CharField '), ('User.userchannels.payment.account_name', 'account_name: CharField '), ('User.userchannels.payment.bank_name', 'bank_name: CharField '), ('User.userchannels.payment.transfer_note', 'transfer_note: CharField '), ('User.userchannels.payment.currency', 'currency: CharField '), ('User.userchannels.payment.recipient_message', 'recipient_message: CharField '), ('User.userchannels.payment.operation_id', 'operation_id: CharField '), ('User.userchannels.payment.transfer_type', 'transfer_type: CharField '), ('User.userchannels.payment.specification', 'specification: CharField '), ('User.userchannels.payment.order_id', 'order_id: CharField '), ('User.userchannels.payment.user_donor_payment_channel', 'user_donor_payment_channel: ForeignKey '), ('User.userchannels.payment.account_statement', 'account_statement: ForeignKey '), ('User.userchannels.payment.created', 'created: DateTimeField '), ('User.userchannels.payment.updated', 'updated: DateTimeField ')]), ('User.userchannels.last_payment', [('User.userchannels.last_payment.id', 'id: AutoField '), ('User.userchannels.last_payment.date', 'date: DateField '), ('User.userchannels.last_payment.amount', 'amount: PositiveIntegerField '), ('User.userchannels.last_payment.account', 'account: CharField '), ('User.userchannels.last_payment.bank_code', 'bank_code: CharField '), ('User.userchannels.last_payment.VS', 'VS: CharField '), ('User.userchannels.last_payment.VS2', 'VS2: CharField '), ('User.userchannels.last_payment.SS', 'SS: CharField '), ('User.userchannels.last_payment.KS', 'KS: CharField '), ('User.userchannels.last_payment.BIC', 'BIC: CharField '), ('User.userchannels.last_payment.user_identification', 'user_identification: CharField '), ('User.userchannels.last_payment.type', "type: CharField ('bank-transfer', 'cash', 'expected', 'darujme')"), ('User.userchannels.last_payment.done_by', 'done_by: CharField '), ('User.userchannels.last_payment.account_name', 'account_name: CharField '), ('User.userchannels.last_payment.bank_name', 'bank_name: CharField '), ('User.userchannels.last_payment.transfer_note', 'transfer_note: CharField '), ('User.userchannels.last_payment.currency', 'currency: CharField '), ('User.userchannels.last_payment.recipient_message', 'recipient_message: CharField '), ('User.userchannels.last_payment.operation_id', 'operation_id: CharField '), ('User.userchannels.last_payment.transfer_type', 'transfer_type: CharField '), ('User.userchannels.last_payment.specification', 'specification: CharField '), ('User.userchannels.last_payment.order_id', 'order_id: CharField '), ('User.userchannels.last_payment.user_donor_payment_channel', 'user_donor_payment_channel: ForeignKey '), ('User.userchannels.last_payment.account_statement', 'account_statement: ForeignKey '), ('User.userchannels.last_payment.created', 'created: DateTimeField '), ('User.userchannels.last_payment.updated', 'updated: DateTimeField ')]), ('User.userchannels', [('User.userchannels.id', 'id: AutoField '), ('User.userchannels.VS', 'VS: CharField '), ('User.userchannels.SS', 'SS: CharField '), ('User.userchannels.user', 'user: ForeignKey '), ('User.userchannels.registered_support', 'registered_support: DateTimeField '), ('User.userchannels.regular_frequency', "regular_frequency: CharField ('monthly', 'quaterly', 'biannually', 'annually', None)"), ('User.userchannels.expected_date_of_first_payment', 'expected_date_of_first_payment: DateField '), ('User.userchannels.regular_amount', 'regular_amount: PositiveIntegerField '), ('User.userchannels.exceptional_membership', 'exceptional_membership: BooleanField '), ('User.userchannels.regular_payments', "regular_payments: CharField ('regular', 'onetime', 'promise')"), ('User.userchannels.old_account', 'old_account: BooleanField '), ('User.userchannels.other_support', 'other_support: TextField '), ('User.userchannels.money_account', 'money_account: ForeignKey '), ('User.userchannels.user_bank_account', 'user_bank_account: ForeignKey '), ('User.userchannels.event', 'event: ForeignKey '), ('User.userchannels.end_of_regular_payments', 'end_of_regular_payments: DateField '), ('User.userchannels.number_of_payments', 'number_of_payments: IntegerField '), ('User.userchannels.last_payment', 'last_payment: DenormDBField '), ('User.userchannels.expected_regular_payment_date', 'expected_regular_payment_date: DateField '), ('User.userchannels.payment_total', 'payment_total: FloatField '), ('User.userchannels.extra_money', 'extra_money: IntegerField '), ('User.userchannels.no_upgrade', 'no_upgrade: NullBooleanField ')])], help_text='Value or variable on left-hand side', max_length=50, null=True, verbose_name='Variable'),
        ),
    ]
