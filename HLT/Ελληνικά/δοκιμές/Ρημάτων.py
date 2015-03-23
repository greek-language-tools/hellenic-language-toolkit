#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, dimitriadis dimitris
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the dimitriadis dimitris nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL dimitriadis dimitris BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ναι = True
όχι = False
λίστα = list
εύρος = range
μήκος = len
τίποτα = None
τύπωσε = print
κείμενο  = str
ακέραιος = int

class Δοκιμές_Ρημάτων():
	def __init__(self, γραμματική, δεδομένα):
		self.ρήματα = γραμματική.ρήματα
		self.αναγνώριση = γραμματική.αναγνώριση
		self.ρ = self.ρήματα

		self.δεδομένα_κλίσης = δεδομένα.κ["ρήμα"]
		self.χρόνοι_κλάση = {
			"ενεστώτας":     self.ρήματα.ενεστώτας,
			"παρατατικός":   self.ρήματα.παρατατικός,
			"αόριστος":      self.ρήματα.αόριστος,
			"παρακείμενος":  self.ρήματα.παρακείμενος,
			"υπερσυντέλικος":self.ρήματα.υπερσυντέλικος,
			"μέλλοντας":     self.ρήματα.μέλλοντας,
			"συντελεσμένος μέλλοντας":self.ρήματα.συντελεσμένος_μέλλοντας}
		self.χρόνοι    = {
			0:"ενεστώτας",   3:"παρακείμενος",
			1:"παρατατικός", 2:"αόριστος"}
		self.αριθμοί = {"ενικός":0, "δυϊκός":1, "πληθυντικός":2}
		self.πρόσωπα = {  "α":0, "β":1, "γ":2}

	def δοκιμές_αναγνώρισης(self):
		# αναγνώριση
		δ1, α1 = self.αναγνώριση_ενεστώτα()
		δ2, α2 = self.αναγνώριση_παρατατικού()
		δ3, α3 = self.αναγνώριση_αορίστου()
		δ4, α4 = self.αναγνώριση_παρακείμενου()
		δ5, α5 = self.αναγνώριση_υπερσυντέλικου()
		δ6, α6 = self.αναγνώριση_μέλλοντα()
		δ7, α7 = self.αναγνώριση_συντελεσμένου_μέλλοντα()
		δ = δ1 + δ2 + δ3 + δ4 + δ5 + δ6 + δ7
		α = α1 + α2 + α3 + α4 + α5 + α6 + α7
		print('Αναγνώριση Ρημάτων: Δοκιμές %d  Αποτυχίες %d' % (δ,α))

	def δοκιμές_κλίσης(self):
		# κλίση
		δ1, α1 = self.κλίση_ενεστώτα()
		δ2, α2 = self.κλίση_παρατατικού()
		δ3, α3 = self.κλίση_αορίστου()
		δ4, α4 = self.κλίση_παρακείμενου()
		δ5, α5 = self.κλίση_υπερσυντέλικου()
		δ6, α6 = self.κλίση_μέλλοντα()
		δ7, α7 = self.κλίση_συντελεσμένου_μέλλοντα()
		δ = δ1 + δ2 + δ3 + δ4 + δ5 + δ6 + δ7
		α = α1 + α2 + α3 + α4 + α5 + α6 + α7
		print('Κλίση Ρημάτων: Δοκιμές %d  Αποτυχίες %d' % (δ,α))

	# κλίση
	def κλίση_ενεστώτα(self):
		δ1, α1 = self.__κλίση("ενεστώτας", 'οριστική')
		δ2, α2 = self.__κλίση("ενεστώτας", 'υποτακτική')
		δ3, α3 = self.__κλίση("ενεστώτας", 'ευκτική')
		δ4, α4 = self.__κλίση("ενεστώτας", 'προστακτική')
		δ5, α5 = self.__κλίση_άλλο("ενεστώτας", 'απαρέμφατο')
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΚΛΙΣΗ Ενεστώτα: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
		
	def κλίση_μέλλοντα(self):
		δ1, α1 = self.__κλίση("μέλλοντας", 'οριστική')
		δ3, α3 = self.__κλίση("μέλλοντας", 'ευκτική')
		δ5, α5 = self.__κλίση_άλλο("μέλλοντας", 'απαρέμφατο')
		δ = δ1 + δ3 + δ5
		α = α1 + α3 + α5
		print('ΚΛΙΣΗ Μέλλοντα": Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
	
	def κλίση_συντελεσμένου_μέλλοντα(self):
		δ1, α1 = self.__κλίση("συντελεσμένος μέλλοντας", 'οριστική')
		δ3, α3 = self.__κλίση("συντελεσμένος μέλλοντας", 'ευκτική')
		δ5, α5 = self.__κλίση_άλλο("συντελεσμένος μέλλοντας", 'απαρέμφατο')
		δ = δ1 + δ3 + δ5
		α = α1 + α3 + α5
		print('ΚΛΙΣΗ Συντελεσμένου Μέλλοντα": Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def κλίση_παρατατικού(self):
		δ, α = self.__κλίση("παρατατικός", 'οριστική')
		print('ΚΛΙΣΗ Παρατατικού: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
		
	def κλίση_υπερσυντέλικου(self):
		δ, α = self.__κλίση("υπερσυντέλικος", 'οριστική')
		print('ΚΛΙΣΗ Υπερσυντέλικου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def κλίση_αορίστου(self):
		δ1, α1 = self.__κλίση("αόριστος", 'οριστική')
		δ2, α2 = self.__κλίση("αόριστος", 'υποτακτική')
		δ3, α3 = self.__κλίση("αόριστος", 'ευκτική')
		δ4, α4 = self.__κλίση("αόριστος", 'προστακτική')
		δ5, α5 = self.__κλίση_άλλο("αόριστος", "απαρέμφατο")
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΚΛΙΣΗ Αορίστου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def κλίση_παρακείμενου(self):
		δ1, α1 = self.__κλίση("παρακείμενος", 'οριστική')
		δ2, α2 = self.__κλίση("παρακείμενος", 'υποτακτική')
		δ3, α3 = self.__κλίση("παρακείμενος", 'ευκτική')
		δ4, α4 = self.__κλίση("παρακείμενος", 'προστακτική')
		δ5, α5 = self.__κλίση_άλλο("παρακείμενος", "απαρέμφατο")
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΚΛΙΣΗ Παρακείμενου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def __κλίση_άλλο(self, χρόνος, έγκλιση, δείξε=False):
		δοκιμασμένα, αποτυχίες = 0, 0
		for διάλεκτος, λέξεις in self.δεδομένα_κλίσης.items():
			for λέξη in λέξεις:
				if χρόνος in λέξεις[λέξη]:
					φωνές =  λέξεις[λέξη][χρόνος]
					for φωνή in φωνές:
						if έγκλιση in φωνές[φωνή]:
							αναμενόμενο =  φωνές[φωνή][έγκλιση][0]
		
							αποτελέσματα = self.χρόνοι_κλάση[χρόνος](λέξη, φωνή, έγκλιση, διάλεκτος=διάλεκτος)
							if αποτελέσματα!=τίποτα:
								OK = False
								for στοιχείο in αναμενόμενο:
									if στοιχείο not in αποτελέσματα:
										OK = True
								if OK:
									τύπωσε(λέξη, φωνή, έγκλιση)
									τύπωσε( "ΑΠΟΤΕΛΕΣΜΑ:", αποτελέσματα, "   ΑΝΑΜΕΝΟΤΑΝ:", αναμενόμενο)
									αποτυχίες += 1
								δοκιμασμένα += 1

		if δείξε or αποτυχίες>0:
			τύπωσε("Δοκιμές κλίσης:", χρόνος,έγκλιση)
			τύπωσε("Δοκιμές:",δοκιμασμένα," Αποτυχίες:", αποτυχίες)
		return [δοκιμασμένα, αποτυχίες]

	def __κλίση(self, χρόνος, έγκλιση, δείξε=False):
		δοκιμασμένα, αποτυχίες = 0, 0
		for διάλεκτος, λέξεις in self.δεδομένα_κλίσης.items():
			for λέξη in λέξεις:
				if χρόνος in λέξεις[λέξη]:
					φωνές =  λέξεις[λέξη][χρόνος]
					for φωνή in φωνές:
						if έγκλιση in φωνές[φωνή]:
							δοκιμές =  φωνές[φωνή][έγκλιση]
							δείκτης_αριθμού = 0
							for αριθμός in ['ενικός', 'δυϊκός', 'πληθυντικός']:
								δείκτης_προσώπου = 0
								for πρόσωπο in ['α', 'β', 'γ']:
									αναμενόμενο =  δοκιμές[δείκτης_αριθμού*3+δείκτης_προσώπου]
		
									if έγκλιση in ['οριστική', 'υποτακτική', 'ευκτική', 'προστακτική']:
										if χρόνος in ["παρατατικός", "υπερσυντέλικος"]:
											αποτελέσματα = self.χρόνοι_κλάση[χρόνος](λέξη, φωνή, αριθμός, πρόσωπο, διάλεκτος)
										else:
											αποτελέσματα = self.χρόνοι_κλάση[χρόνος](λέξη, φωνή, έγκλιση, αριθμός, πρόσωπο, διάλεκτος=διάλεκτος)
									if αποτελέσματα!=τίποτα:
										OK = False
										for στοιχείο in αναμενόμενο:
											if στοιχείο not in αποτελέσματα:
												OK = True
										if OK:
											τύπωσε(λέξη, διάλεκτος, χρόνος, φωνή, έγκλιση, αριθμός, πρόσωπο)
											τύπωσε( "ΑΠΟΤΕΛΕΣΜΑ:", αποτελέσματα, "   ΑΝΑΜΕΝΟΤΑΝ:", αναμενόμενο)
											if χρόνος in ["παρατατικός", "υπερσυντέλικος"]:
												τύπωσε(self.χρόνοι_κλάση[χρόνος](λέξη, φωνή, αριθμός, πρόσωπο, διάλεκτος))
											else:
												τύπωσε(self.χρόνοι_κλάση[χρόνος](λέξη, φωνή, έγκλιση, αριθμός, πρόσωπο, διάλεκτος=διάλεκτος))
											αποτυχίες += 1
										δοκιμασμένα += 1
									δείκτης_προσώπου += 1
								δείκτης_αριθμού += 1

		if δείξε or αποτυχίες>0:
			if έγκλιση:
				τύπωσε("Δοκιμές κλίσης:", χρόνος,έγκλιση)
			else:
				τύπωσε("Δοκιμές κλίσης:", χρόνος)
			τύπωσε("Δοκιμές:",δοκιμασμένα," Αποτυχίες:", αποτυχίες)
		return [δοκιμασμένα, αποτυχίες]

	# αναγνώριση
	def αναγνώριση_ενεστώτα(self):
		δ1, α1 = self.__αναγνώριση("ενεστώτας", 'οριστική')
		δ2, α2 = self.__αναγνώριση("ενεστώτας", 'υποτακτική')
		δ3, α3 = self.__αναγνώριση("ενεστώτας", 'ευκτική')
		δ4, α4 = self.__αναγνώριση("ενεστώτας", 'προστακτική')
		δ5, α5 = self.__αναγνώριση_άλλο("ενεστώτας", 'απαρέμφατο')
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΑΝΑΓΝΩΡΙΣΗ Ενεστώτα: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def αναγνώριση_παρατατικού(self):
		δ, α = self.__αναγνώριση("παρατατικός", 'οριστική')
		print('ΑΝΑΓΝΩΡΙΣΗ Παρατατικού: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
		
	def αναγνώριση_υπερσυντέλικου(self):
		δ, α = self.__αναγνώριση("υπερσυντέλικος", 'οριστική')
		print('ΑΝΑΓΝΩΡΙΣΗ Υπερσυντέλικου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def αναγνώριση_αορίστου(self):
		δ1, α1 = self.__αναγνώριση("αόριστος", 'οριστική')
		δ2, α2 = self.__αναγνώριση("αόριστος", 'υποτακτική')
		δ3, α3 = self.__αναγνώριση("αόριστος", 'ευκτική')
		δ4, α4 = self.__αναγνώριση("αόριστος", 'προστακτική')
		δ5, α5 = self.__αναγνώριση_άλλο("αόριστος", 'απαρέμφατο')
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΑΝΑΓΝΩΡΙΣΗ Αορίστου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def αναγνώριση_παρακείμενου(self):
		δ1, α1 = self.__αναγνώριση("παρακείμενος", 'οριστική')
		δ2, α2 = self.__αναγνώριση("παρακείμενος", 'υποτακτική')
		δ3, α3 = self.__αναγνώριση("παρακείμενος", 'ευκτική')
		δ4, α4 = self.__αναγνώριση("παρακείμενος", 'προστακτική')
		δ5, α5 = self.__αναγνώριση_άλλο("παρακείμενος", 'απαρέμφατο')
		δ = δ1 + δ2 + δ3 + δ4 + δ5
		α = α1 + α2 + α3 + α4 + α5
		print('ΑΝΑΓΝΩΡΙΣΗ Παρακείμενου: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
		
	def αναγνώριση_μέλλοντα(self):
		δ1, α1 = self.__αναγνώριση("μέλλοντας", 'οριστική')
		δ3, α3 = self.__αναγνώριση("μέλλοντας", 'ευκτική')
		δ5, α5 = self.__αναγνώριση_άλλο("μέλλοντας", 'απαρέμφατο')
		δ = δ1 + δ3 + δ5
		α = α1 + α3 + α5
		print('ΑΝΑΓΝΩΡΙΣΗ Μέλλοντα: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]
	
	def αναγνώριση_συντελεσμένου_μέλλοντα(self):
		δ1, α1 = self.__αναγνώριση("συντελεσμένος μέλλοντας", 'οριστική')
		δ3, α3 = self.__αναγνώριση("συντελεσμένος μέλλοντας", 'ευκτική')
		δ5, α5 = self.__αναγνώριση_άλλο("συντελεσμένος μέλλοντας", 'απαρέμφατο')
		δ = δ1 + δ3 + δ5
		α = α1 + α3 + α5
		print('ΑΝΑΓΝΩΡΙΣΗ Συντελεσμένου Μέλλοντα: Δοκιμές %d  Αποτυχίες %d' % (δ,α))
		return [δ, α]

	def __αναγνώριση_άλλο(self, χρόνος, έγκλιση, δείξε=False):
		δοκιμασμένα, αποτυχίες = 0, 0
		for διάλεκτος, λέξεις in self.δεδομένα_κλίσης.items():
			for λέξη in λέξεις:
				if χρόνος in λέξεις[λέξη]:
					φωνές =  λέξεις[λέξη][χρόνος]
					for φωνή in φωνές:
						if έγκλιση in φωνές[φωνή]:
							δοκιμές =  φωνές[φωνή][έγκλιση][0]
	
							λεξικό = {
								'έγκλιση':έγκλιση, 'φωνή':φωνή,
								'χρόνος':χρόνος, 'διάλεκτος':διάλεκτος,
								'μέρος του λόγου':"ρήμα"
								}
							for υδοκιμή in δοκιμές:
								αποτελέσματα = self.αναγνώριση(υδοκιμή, διάλεκτος)
								σύνολο =[]
								μόριο, θέμα = '', υδοκιμή
	
								for αποτέλεσμα in αποτελέσματα:
									if αποτέλεσμα["μέρος του λόγου"]!="ρήμα":
										continue
									αστοχίες = self.__σύγκριση_λεξικών(λεξικό, αποτέλεσμα, θέμα)
									if αστοχίες:
										σύνολο.append(αστοχίες)
									else:
										σύνολο.append("Επιτυχία")
								if σύνολο and not "Επιτυχία" in σύνολο:
									τύπωσε(λέξη, δοκιμές,φωνή)
									#τύπωσε(αποτελέσματα)
									for στοιχείο in σύνολο:
										if στοιχείο!="Επιτυχία":
											for κ,τ in στοιχείο.items():
												τύπωσε(κ, "ΑΠΟΤΕΛΕΣΜΑ:", τ[1], "   ΑΝΑΜΕΝΟΤΑΝ:", τ[0])
											τύπωσε()
									αποτυχίες += 1
								δοκιμασμένα += 1
				if δείξε or αποτυχίες>0:
					if έγκλιση:
						τύπωσε("Δοκιμές αναγνώρισης:", χρόνος,έγκλιση)
					else:
						τύπωσε("Δοκιμές αναγνώρισης:", χρόνος)
					τύπωσε("Δοκιμές:",δοκιμασμένα," Αποτυχίες:", αποτυχίες)
		return [δοκιμασμένα, αποτυχίες]

	def __σύγκριση_λεξικών(self, λεξικό, αποτέλεσμα, λέξη):
		αστοχίες = {}
		αλέξη = self.ρ.τονιστής.κωδικοποιητής(λέξη)
		self.ρ.τονιστής.αφαίρεσε_τόνους(αλέξη)
		αλέξη = self.ρ.τονιστής.απόκωδικοποιητής(αλέξη, True)

		for k,v in λεξικό.items():
			if k not in αποτέλεσμα:
				αστοχίες[k] = [v, 'Τίποτα']
			else:
				if v!=αποτέλεσμα[k]:
					αστοχίες[k] = [v, αποτέλεσμα[k]]
		if 'κατάληξη' in αποτέλεσμα:
			if "ανώμαλο" in αποτέλεσμα:
				if not λέξη==αποτέλεσμα['κατάληξη']:
					αστοχίες['κατάληξη'] = [λέξη, αποτέλεσμα['κατάληξη']]
			elif not αλέξη.endswith(αποτέλεσμα['κατάληξη']):
				αστοχίες['κατάληξη'] = [αλέξη, αποτέλεσμα['κατάληξη']]
		if 'συνθετικό' in αποτέλεσμα and\
			αποτέλεσμα['συνθετικό']:
			if not αλέξη.startswith(αποτέλεσμα['συνθετικό']):
				if 'αύξηση' in αποτέλεσμα and\
					αποτέλεσμα['αύξηση'] and\
					not αλέξη.startswith(αποτέλεσμα['αύξηση']):
					αστοχίες['συνθετικό'] = [λέξη, αποτέλεσμα['συνθετικό']]
		if 'θέμα' in αποτέλεσμα:
			if not (αποτέλεσμα['θέμα'] in λέξη or\
				αποτέλεσμα['θέμα'] in αλέξη):
				αστοχίες['θέμα'] = [αλέξη, αποτέλεσμα['θέμα']]
		return αστοχίες

	def __αναγνώριση(self, χρόνος, έγκλιση, δείξε=False):
		δοκιμασμένα, αποτυχίες = 0, 0
		for διάλεκτος, λέξεις in self.δεδομένα_κλίσης.items():
			for λέξη in λέξεις:
				if χρόνος in λέξεις[λέξη]:
					φωνές =  λέξεις[λέξη][χρόνος]
					for φωνή in φωνές:
						if έγκλιση in φωνές[φωνή]:
							δοκιμές =  φωνές[φωνή][έγκλιση]
							for αριθμός in ['ενικός', 'δυϊκός', 'πληθυντικός']:
								for πρόσωπο in ['α', 'β', 'γ']:
									δοκιμή =  δοκιμές[self.αριθμοί[αριθμός]*3+self.πρόσωπα[πρόσωπο]]
	
									λεξικό = {'αριθμός':αριθμός, 'πρόσωπο':πρόσωπο,
												'έγκλιση':έγκλιση, 'φωνή':φωνή,
												'χρόνος':χρόνος, 'διάλεκτος':διάλεκτος,
												'μέρος του λόγου':"ρήμα"
												}
									
									for υδοκιμή in δοκιμή:
										αποτελέσματα = self.αναγνώριση(υδοκιμή, διάλεκτος)
										σύνολο =[]
										θέμα = υδοκιμή
	
										for αποτέλεσμα in αποτελέσματα:
											if αποτέλεσμα["μέρος του λόγου"]!="ρήμα" or\
												αποτέλεσμα["διάλεκτος"]!=διάλεκτος:
												continue
											αστοχίες = self.__σύγκριση_λεξικών(λεξικό, αποτέλεσμα, θέμα)
											if αστοχίες:
												σύνολο.append(αστοχίες)
											else:
												σύνολο.append("Επιτυχία")
										if not αποτελέσματα and υδοκιμή:
											αστοχίες = self.__σύγκριση_λεξικών(λεξικό, {}, θέμα)
											σύνολο.append(αστοχίες)
											
										if σύνολο and not "Επιτυχία" in σύνολο:
											τύπωσε(λέξη, υδοκιμή, χρόνος, φωνή, έγκλιση, αριθμός, πρόσωπο, διάλεκτος)
											#τύπωσε('θέμα',bb['θέμα'])
											#	τύπωσε('κατάληξη',bb['κατάληξη'])
											#	τύπωσε('τονισμός',bb['τονισμός'])
											#	τύπωσε('διάλεκτος',bb['διάλεκτος'])
											#	τύπωσε('χρόνος',bb['χρόνος'])
											#	τύπωσε('κατηγορία',bb['κατηγορία'])
											#	τύπωσε('έγκλιση',bb['έγκλιση'])
											#	τύπωσε('αριθμός',bb['αριθμός'])
											#	τύπωσε('πρόσωπο',bb['πρόσωπο'])
											#τύπωσε(αποτελέσματα)
											for στοιχείο in σύνολο:
												if στοιχείο!="Επιτυχία":
													for κ,τ in στοιχείο.items():
														τύπωσε(κ, "ΑΠΟΤΕΛΕΣΜΑ:", τ[1], "   ΑΝΑΜΕΝΟΤΑΝ:", τ[0])
													τύπωσε()
											αποτυχίες += 1
										δοκιμασμένα += 1
				
		return [δοκιμασμένα, αποτυχίες]
