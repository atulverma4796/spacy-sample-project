import spacy

# nlp_new = spacy.load(R"./output/model-best") 

# text = 'POLICY NUMBER: HXMP101057 COMMERCIAL GENERAL LIABILITY CG 21 53 01 96 THIS ENDORSEMENT CHANGES THE POLICY. PLEASE READ IT CAREFULLY. EXCLUSION -DESIGNATED ONGOING OPERATIONS This endorsement modifies insurance provided under the following: COMMERCIAL GENERAL LIABILITY COVERAGE PART SCHEDULE Description of Designated Ongoing Operation(s): Any Exterior Work in Excess of 2 Stories Specified Location (If Applicable): (If no entry appears above, information required to complete this endorsement will be shown in the Declarations as applicable to this endorsement.) The following exclusion is added to paragraph 2., Exclusions of COVERAGE A -BODILY INJURY AND PROPERTY DAMAGE LIABILITY (Section I -Coverages): This insurance does not apply to "bodily injury" or "property damage" arising out of the ongoing operations described in the Schedule of this endorsement, regardless of whether such operations are conducted by you or on your behalf or whether the operations are conducted for yourself or for others. Unless a "location" is specified in the Schedule, this exclusion applies regardless of where such operations are conducted by you or on your behalf. If a specific "location" is designated in the Schedule of this endorsement, this exclusion applies only to the described ongoing operations conducted at that "location". For the purpose of this endorsement, "location" means premises involving the same or connecting lots, or premises whose connection is interrupted only by a street, roadway, waterway or right-of-way of a railroad. CG 21 53 01 96 Copyright, Insurance Services Office, Inc., 1994 Page 1 of 1'
# tokens = nlp_new(text) 
# # print('tokens: ', tokens)
# # print([(X, X.ent_iob_, X.ent_type_) for X in tokens])

# print([(X, X.entity) for X in tokens])


# nlp = spacy.load("en_core_web_sm")

# trained_nlp = spacy.load("./output/model-best")

trained_nlp = spacy.load("./output/model-last")

# text = 'POLICY NUMBER: COMMERCIAL GENERAL LIABILITY CG 25 03 05 09 THIS ENDORSEMENT CHANGES THE POLICY. PLEASE READ IT CAREFULLY. DESIGNATED CONSTRUCTION PROJECT(S) GENERAL AGGREGATE LIMIT This endorsement modifies insurance provided under the following: COMMERCIAL GENERAL LIABILITY COVERAGE PART SCHEDULE Designated Construction Project(s): All Construction Projects During The Policy Term. Information required to complete this Schedule, if not shown above, will be shown in the Declarations . A. For all sums which the insured becomes legally obligated to pay as damages caused by "occurrences" under Section I -Coverage A, and for all medical expenses caused by accidents under Section I -Coverage C, which can be attributed only to ongoing operations at a single designated construction project shown in the Schedule above: 1. A separate Designated Construction Project General Aggregate Limit applies to each designated construction project, and that limit is equal to the amount of the General Aggregate Limit shown in the Declarations . 2. The Designated Construction Project General Aggregate Limit is the most we will pay for the sum of all damages under Coverage A, except damages because of "bodily injury" or "property damage" included in the "productscompleted operations hazard", and for medical expenses under Coverage C regardless of the number of: a. Insureds; b. Claims made or "suits" brought; or c. Persons or organizations making claims or bringing "suits". 3. Any payments made under Coverage A for damages or under Coverage C for medical expenses shall reduce the Designated Construction Project General Aggregate Limit for that designated construction project. Such payments shall not reduce the General Aggregate Limit shown in the Declarations nor shall they reduce any other Designated Construction Project General Aggregate Limit for any other designated construction project shown in the Schedule above. 4. The limits shown in the Declarations for Each Occurrence, Damage To Premises Rented To You and Medical Expense continue to apply. However, instead of being subject to the General Aggregate Limit shown in the Declarations, such limits will be subject to the applicable Designated Construction Project General Aggregate Limit. CG 25 03 05 09 ©Insurance Services Office, Inc., 2008 Page 1of2 D'

# text = 'POLICY NUMBER:  1-TPM -NY-17-01234898  COMMERCIAL GENERAL LIABILITY   CG 20 12 04 13   THIS ENDORSEMENT CHANGES THE POLICY.  PLEASE READ IT CAREFULLY.  CG 20 12 04 13  © Insurance Services Office, Inc.,  2012  Page 1 of 1   ADDITIONAL INSURED – STATE OR GOVERNMENTAL  AGENCY OR SUBDIVISION OR POLITICAL  SUBDIVISION – PERMITS OR AUTHORIZATIONS  This endorsement modifies insurance provided under the following:  COMMERCIAL GENERAL LIABILITY COVERAGE PART  SCHEDULE  State Or Gove rnmental Agency Or Subdivision Or Political Subdivision:  As Required by Written Contract executed prior to any claim or “suit.”    Information required to complete this Schedule, if not shown above, will be shown in the Declarations.'

text = 'POLICY NUMBER:  1-TPM -NY-17-01234898  COMMERCIAL GENERAL LIABILITY   CG 04 35 12 07   THIS ENDORSEMENT CHANGES THE POLICY.  PLEASE READ IT CAREFULLY.  CG 04 35 12 07  © ISO Properties,  Inc., 2006   Page 1 of 7   EMPLOYEE BENEFITS LIABILITY COVERAGE  THIS ENDORSEMENT PROVIDES CLAIMS-MADE COVERAGE. PLEASE READ THE ENTIRE ENDORSEMENT CAREFULLY.  This endorsement modifies insurance provided under the following:   COMMERCIAL GENERAL LIABILITY COVERAGE PART   SCHEDULE  Coverage  Limit Of Insurance  Each Employee Deductible  Premium  Employee Benefits Programs  $ 1,000,000  each e mployee  $ 1,000  $ Included  $ 1,000,000  aggregate  Retroactive Date:  05/01/2018  Information required to complete this Schedule, if not shown a bove, will be shown i n the Declarations.'

doc = trained_nlp(text)

print('doc.ents: ', doc.ents)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
if len(doc.ents) == 0:
    print ("No entities found.")