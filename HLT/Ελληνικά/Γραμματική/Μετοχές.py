#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012, dimitriadis dimitris
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

import numpy as np

τύπωσε = print

class Μετοχές():
	def __init__(self, τονιστής, δεδομένα, αναγνώριση, ρήματα):
		self.τ = τονιστής
		self.ρήματα = ρήματα
		self.τονιστής = τονιστής
		
		self.δεδομένα = δεδομένα
		self.δ = self.δεδομένα
		self.α = αναγνώριση
		self._αναγνώριση = αναγνώριση
		self.__μεταβλητές()
	
	def __μεταβλητές(self):
		self.δοκιμές = {}
		self.dump_μετοχές = {}
		self.φωνές = { "ενεργητική":0, "μέση":3, "παθητική":6}
		self.αριθμό_σε_φωνή = { 0:"ενεργητική", 1:"μέση", 2:"παθητική"}
		self.γένος_σε_αριθμό = { "αρσενικό":0, "θηλυκό":1, "ουδέτερο":2 }
		self.αριθμό_σε_γένος  = { 0:"αρσενικό",   1:"θηλυκό",   2:"ουδέτερο"   }
		self.αριθμό_σε_πτώση  = { 0:"ονομαστική",   1:"γενική",   2:"δοτική",   3:"αιτιατική",   4:"κλητική"   }
		self.πτώση_σε_αριθμό  = {   "ονομαστική":0,   "γενική":1,   "δοτική":2,   "αιτιατική":3,   "κλητική":4 }
		self.αριθμό_σε_αριθμό = { 0:"ενικός",   1:"δυϊκός",   2:"πληθυντικός"    }
		self.αριθμοί          = {   "ενικός":0,   "δυϊκός":5,    "πληθυντικός":10 }
	
	def dump(self, διάλεκτος=None, λέξη=None):
		αποτέλεσμα = []
		if λέξη:
			if not διάλεκτος in self.dump_μετοχές:
				self.dump()
			offset = None
			if λέξη in self.dump_μετοχές[διάλεκτος]:
				offset = self.dump_μετοχές[διάλεκτος][λέξη]
				if offset>=0:
					γκΛέξη = self.δ.δ["θέματα"][offset]["κΛέξη"]
					κατηγορία = 0
					σύνολο = self.δ.δ["θέματα"][offset]
					κΣυνθετικό = σύνολο.get("κΣυνθετικό")
					κΑύξηση = σύνολο.get("κΑύξηση")
					κΑύξηση_παρακείμενου = σύνολο.get("κΑύξηση_παρακείμενου")
					κΕνεστωτική_αύξηση = σύνολο.get("κΕνεστωτική_αύξηση")
					κλίσεις = {}
					if "μετοχή" not in self.δ.δ["θέματα"][offset]:
						return αποτέλεσμα
					for χρόνο in self.δ.δ["θέματα"][offset]["μετοχή"]:
						if χρόνο not in ["ενεστώτας", "παρατατικός", "αόριστος",	"παρακείμενος",
												"υπερσυντέλικος",	"μέλλοντας", "συντελεσμένος μέλλοντας"]:
							continue
						if χρόνο not in σύνολο["μετοχή"] or\
							σύνολο["μετοχή"][χρόνο]==0 or\
							sum(σύνολο["μετοχή"][χρόνο]["καταλήξεις"])==0:
							continue
						κλίσεις[χρόνο] = {}
						for φωνή in ["ενεργητική", "μέση", "παθητική"]:
							if sum(σύνολο["μετοχή"][χρόνο]["καταλήξεις"][self.φωνές[φωνή]:self.φωνές[φωνή]+3])==0:
								continue
							κλίσεις[χρόνο][φωνή] = {}
							for γένος in ["αρσενικό", "θηλυκό", "ουδέτερο"]:
								κλίσεις[χρόνο][φωνή][γένος] = []
								for αριθμός in ["ενικός", "δυϊκός", "πληθυντικός"]:
									for πτώση in ["ονομαστική", "γενική", "δοτική", "αιτιατική", "κλητική"]:
										κΛέξεις = self.__κλίνε(γκΛέξη, κατηγορία, σύνολο["μετοχή"], αριθμός, πτώση,
											 γένος, χρόνο, φωνή, διάλεκτος, 
											 κΣυνθετικό, κΑύξηση, κΑύξηση_παρακείμενου, κΕνεστωτική_αύξηση)
										λέξεις = []
										for κΛέξη in κΛέξεις:
											λέξεις.append(self.τ.απο(κΛέξη, True))
										κλίσεις[χρόνο][φωνή][γένος].append(λέξεις)
					αποτέλεσμα = κλίσεις
				else:
					κατηγορία = abs(offset+1)
					if "μετοχή" in self.δ.δ["ανώμαλα"]["ρήμα"][διάλεκτος][κατηγορία]:
						αποτέλεσμα = self.δ.δ["ανώμαλα"]["ρήμα"][διάλεκτος][κατηγορία]["μετοχή"]
		else:
			self.dump_μετοχές.clear()
			# προσθήκη ανώμαλων
			
			for διάλεκτος, σύνολα in self.δ.δ["ανώμαλα"]["ρήμα"].items():
				ακατηγορία = -1
				self.dump_μετοχές[διάλεκτος] = {}
				for σύνολο in σύνολα:
					ακατηγορία += 1
					if "μετοχή" in σύνολο and σύνολο["μετοχή"]:
						for χρόνο in σύνολο["μετοχή"]:
							for φωνή in σύνολο["μετοχή"][χρόνο]:
								σλέξεις = σύνολο["μετοχή"][χρόνο][φωνή]["αρσενικό"]["καταλήξεις"][0]
								for σλέξη in σλέξεις:
									if σλέξη in self.dump_μετοχές[διάλεκτος]:
										σλέξη = σλέξη+str(ακατηγορία)
									self.dump_μετοχές[διάλεκτος][σλέξη] = -1-ακατηγορία
							break
						break
				
			γκατηγορία = -1
			for σύνολο in self.δ.δ["θέματα"]:
				γκατηγορία += 1
				if σύνολο["μέρος του λόγου"]=="ρήμα":
					if "μετοχή" not in σύνολο or not σύνολο["μετοχή"]:
						continue
					διάλεκτος = σύνολο["διάλεκτος"]
					if not διάλεκτος in self.dump_μετοχές:
						self.dump_μετοχές[διάλεκτος] = {}
					κΛέξη = σύνολο["κΛέξη"]
					κατηγορία = 0
					κΣυνθετικό = σύνολο.get("κΣυνθετικό")
					κΑύξηση = σύνολο.get("κΑύξηση")
					κΑύξηση_παρακείμενου = σύνολο.get("κΑύξηση_παρακείμενου")
					κΕνεστωτική_αύξηση = σύνολο.get("κΕνεστωτική_αύξηση")
					χρόνος, φωνή = None, None
					for χρόνος in ["ενεστώτας", "παρατατικός", "αόριστος",	"παρακείμενος",
									"υπερσυντέλικος",	"μέλλοντας", "συντελεσμένος μέλλοντας"]:
						if not χρόνος in σύνολο["μετοχή"] or σύνολο["μετοχή"][χρόνος]==0:
							continue
						
						for φ in range(9):
							if σύνολο["μετοχή"][χρόνος]["καταλήξεις"][φ]:
								φωνή = self.αριθμό_σε_φωνή[φ//3]
								break
						if φωνή:
							break
					if σύνολο["μετοχή"][χρόνος]==0:
						continue
					κΛέξεις = self.__κλίνε(κΛέξη, κατηγορία, σύνολο["μετοχή"], "ενικός", "ονομαστική",
					 "αρσενικό", χρόνος, φωνή, διάλεκτος, 
					 κΣυνθετικό, κΑύξηση, κΑύξηση_παρακείμενου, κΕνεστωτική_αύξηση)
					
					for κΛέξη in κΛέξεις:
						σλέξη = self.τ.απο(κΛέξη, True)
						if σλέξη in self.dump_μετοχές[διάλεκτος]:
							σλέξη = σλέξη+str(γκατηγορία)
						self.dump_μετοχές[διάλεκτος][σλέξη] = γκατηγορία
			αποτέλεσμα = {}
			for διάλεκτος, λέξεις in self.dump_μετοχές.items():
				αποτέλεσμα[διάλεκτος] = list(λέξεις.keys())
				αποτέλεσμα[διάλεκτος].sort()
		
		return αποτέλεσμα
	
	def _πλήρη_κλίση(self, αναγνώριση):
		αποτέλεσμα = {}
		κΛέξη = αναγνώριση.get('κΛέξη')
		μετοχή = αναγνώριση.get("μετοχή")
		διάλεκτος = αναγνώριση['διάλεκτος']
		ανώμαλο = αναγνώριση.get("ανώμαλο")
		κΣυνθετικό = αναγνώριση.get("κΣυνθετικό")
		κΑύξηση = αναγνώριση.get("κΑύξηση")
		κΑύξηση_παρακείμενου = αναγνώριση.get("κΑύξηση παρακείμενου")
		κΕνεστωτική_αύξηση = αναγνώριση.get("κΕνεστωτική αύξηση")
		if μετοχή:
			for χρόνος, φωνές in μετοχή.items():
				if χρόνος not in ["ενεστώτας", "παρατατικός", "αόριστος",	"παρακείμενος",
									"υπερσυντέλικος",	"μέλλοντας", "συντελεσμένος μέλλοντας"]:
					continue
				αποτέλεσμα[χρόνος] = {}
				for φωνή in ["ενεργητική", "μέση", "παθητική"]:
					αποτέλεσμα[χρόνος][φωνή] = {}
					for γένος in ["αρσενικό", "θηλυκό", "ουδέτερο"]:
						offset = self.φωνές[φωνή]+self.γένος_σε_αριθμό[γένος]
						if not μετοχή[χρόνος]:
							continue
						if μετοχή[χρόνος]["καταλήξεις"][offset]==0:
							continue
						αποτέλεσμα[χρόνος][φωνή][γένος] = []
						κατηγορία = 0
						for αριθμός in ["ενικός", "δυϊκός", "πληθυντικός"]:
							for πτώση in ["ονομαστική", "γενική", "δοτική", "αιτιατική", "κλητική"]:
								if διάλεκτος=="δημοτική" and\
									(αριθμός=="δυϊκός" or πτώση=="δοτική"):
									αποτέλεσμα[χρόνος][φωνή][γένος].append([])
								else:
									αποτέλεσμα[χρόνος][φωνή][γένος].append(self.__κλίνε(κΛέξη, κατηγορία, μετοχή, αριθμός, πτώση,
							 			γένος, χρόνος, φωνή, διάλεκτος, 
							 			κΣυνθετικό, κΑύξηση, κΑύξηση_παρακείμενου, κΕνεστωτική_αύξηση, ανώμαλο))
					if not αποτέλεσμα[χρόνος][φωνή]:
						del αποτέλεσμα[χρόνος][φωνή]
		return αποτέλεσμα
	
	def __κλίνε(self, κΛέξη, κατηγορία, μετοχή, αριθμός, πτώση,
				 γένος, χρόνος, φωνή, διάλεκτος, 
				 κΣυνθετικό=None, κΑύξηση=None, κΑύξηση_παρακείμενου=None, 
				 κΕνεστωτική_αύξηση=None, ανώμαλο=False):
		κΑποτελέσματα = []
		if χρόνος in [None, 0] or φωνή==None:
			return κΑποτελέσματα
		
		if χρόνος not in self.δ.δ["διάλεκτοι"][διάλεκτος]["μετοχή"] and\
			self.δ.δ["διάλεκτοι"][διάλεκτος]["μετοχή"][χρόνος]:
			return κΑποτελέσματα
		offset = self.φωνές[φωνή]+self.γένος_σε_αριθμό[γένος]
		offset2 = self.πτώση_σε_αριθμό[πτώση]+self.αριθμοί[αριθμός]
		if ανώμαλο:
			σύνολο = self.δ.δ["ανώμαλα"]["ρήμα"][διάλεκτος][κατηγορία]
			
			if χρόνος in σύνολο['καταλήξεις']["μετοχή"] and\
				φωνή in σύνολο['καταλήξεις']["μετοχή"][χρόνος] and\
				γένος in σύνολο['καταλήξεις']["μετοχή"][χρόνος][φωνή]:
				κΑποτελέσματα = σύνολο['καταλήξεις']["μετοχή"][χρόνος][φωνή][γένος]["κΚαταλήξεις"][offset2]
		else:
			καταλήξεις = μετοχή[χρόνος]["καταλήξεις"][offset]
			τονισμοί   = μετοχή[χρόνος]["τονισμοί"][offset]
			if καταλήξεις and\
				"κΚαταλήξεις" in self.δ.δ["καταλήξεις"]["μετοχή"][διάλεκτος][χρόνος][καταλήξεις]:
				if not τονισμοί:
					return κΑποτελέσματα
				if καταλήξεις>10000 :
					if len(self.δοκιμές[διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"])==1:
						κατάληξη = self.δοκιμές[διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"][0]
						if offset2 and self.δ.δ["τονισμοί"]["επίθετο"][διάλεκτος][τονισμοί]["τονισμοί"]:
							τόνος = self.δ.δ["τονισμοί"]["επίθετο"][διάλεκτος][τονισμοί]["τονισμοί"][0]*2
						else:
							τόνος = [0,0,0,0]
					else:
						κατάληξη = self.δοκιμές[διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"][offset2]
						τόνος = self.δ.δ["τονισμοί"]["επίθετο"][διάλεκτος][τονισμοί]["τονισμοί"][offset2]*2
				elif len(self.δ.δ["καταλήξεις"]["μετοχή"][διάλεκτος][χρόνος])<καταλήξεις:
					return κΑποτελέσματα
				elif len(self.δ.δ["καταλήξεις"]["μετοχή"][διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"])==1:
					κατάληξη = self.δ.δ["καταλήξεις"]["μετοχή"][διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"][0]
					τόνος = self.δ.δ["τονισμοί"]["επίθετο"][διάλεκτος][τονισμοί]["τονισμοί"][0]*2
				else:
					κατάληξη = self.δ.δ["καταλήξεις"]["μετοχή"][διάλεκτος][χρόνος][καταλήξεις]["κΚαταλήξεις"][offset2]
					τόνος = self.δ.δ["τονισμοί"]["επίθετο"][διάλεκτος][τονισμοί]["τονισμοί"][offset2]*2
				for υ in range(len(κατάληξη)):
					if χρόνος=="ενεστώτας":
						μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
						if κΕνεστωτική_αύξηση!=None:
							μλέξη = np.append(κΕνεστωτική_αύξηση, μλέξη, 0)
						elif κΣυνθετικό!=None:
							μλέξη = np.append(κΣυνθετικό, μλέξη, 0)
					elif χρόνος=="παρακείμενος":
						μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
						if len(κΛέξη)>1 and\
							κΛέξη[0] == 10 and κΛέξη[1] == 19 and\
							φωνή=="μέση":
							μλέξη = np.append(κΑύξηση, μλέξη, 0)
						elif κΑύξηση_παρακείμενου!=None:
							μλέξη = np.append(κΑύξηση_παρακείμενου, μλέξη, 0)
						elif κΑύξηση!=None:
							μλέξη = np.append(κΑύξηση, μλέξη, 0)
					elif χρόνος=="συντελεσμένος μέλλοντας":
						μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
						if κΛέξη.size>0 and\
							κΛέξη[0] == 10 and κΛέξη[1] == 19 and\
							φωνή=="μέση" and κΑύξηση!=None:
							μλέξη = np.append(κΑύξηση, κΛέξη, 0)
						elif κΑύξηση_παρακείμενου!=None:
							μλέξη = np.append(κΑύξηση_παρακείμενου, μλέξη, 0)
					elif χρόνος=="παρακείμενος": 
						μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
						if κΑύξηση!=None:
							μλέξη = np.append(κΑύξηση, μλέξη, 0)
					elif κΣυνθετικό!=None:
						if κΛέξη==None:
							μλέξη = κατάληξη[υ].__deepcopy__(κατάληξη[υ])
						else:
							μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
						μλέξη = np.append(κΣυνθετικό, μλέξη, 0)
					else:
						if κΛέξη==None:
							μλέξη = κατάληξη[υ].__deepcopy__(κατάληξη[υ])
						else:
							μλέξη = np.append(κΛέξη, κατάληξη[υ], 0)
					self.τ.τόνισε(μλέξη, τόνος[υ])
					if κΛέξη==None or len(κΛέξη)==0:
						self.τ.πρόσθεσε_ψιλή(μλέξη)
					κΑποτελέσματα.append(μλέξη)
		return κΑποτελέσματα
	
	def _κλίνε(self, κΛέξη, αριθμός='ενικός', πτώση='ονομαστική',
				 γένος='αρσενικό', χρόνος=None, φωνή=None, διάλεκτος=None):
		κΑποτελέσματα = []
		if διάλεκτος not in self.δ.δ["διάλεκτοι"]:
			return κΑποτελέσματα
			
		αναγνωρίσεις = self.α._αναγνώριση(κΛέξη, self.δ, διάλεκτος)
		for αναγνώριση in αναγνωρίσεις:
			if αναγνώριση["μέρος του λόγου"]!="μετοχή":
				continue
			if	διάλεκτος and διάλεκτος != αναγνώριση['διάλεκτος']:
				continue
			
			ανώμαλο = αναγνώριση.get("ανώμαλο")
			if "μετοχή" not in αναγνώριση and not ανώμαλο:
				continue
			
			if χρόνος and χρόνος in αναγνώριση["μετοχή"]:
				tχρόνος = χρόνος
			else:
				tχρόνος = αναγνώριση['χρόνος']
			
			if φωνή:
				tφωνή = φωνή
			else:
				if 'φωνή' not in αναγνώριση:
					print(αναγνώριση)
				tφωνή = αναγνώριση['φωνή']
			
			if not ανώμαλο and tχρόνος not in αναγνώριση["μετοχή"]:
				continue
			
			κατηγορία = αναγνώριση.get("κατηγορία")
			κΣυνθετικό = αναγνώριση.get("κΣυνθετικό")
			κΕνεστωτική_αύξηση = αναγνώριση.get("κΕνεστωτική αύξηση")
			κΑύξηση = αναγνώριση.get("κΑύξηση")
			κΑύξηση_παρακείμενου = αναγνώριση.get("κΑύξηση παρακείμενου")
			μετοχή = αναγνώριση.get("μετοχή")
			θέμα = αναγνώριση.get("κΛέξη")
			
			κΑποτελέσματα += self.__κλίνε(θέμα, κατηγορία, μετοχή, αριθμός, πτώση,
				 γένος, tχρόνος, tφωνή, διάλεκτος, 
				 κΣυνθετικό, κΑύξηση, κΑύξηση_παρακείμενου, κΕνεστωτική_αύξηση, ανώμαλο)
			
		return κΑποτελέσματα
	
	def κλίνε(self, λέξη, αριθμός='ενικός', πτώση='ονομαστική',
				 γένος='αρσενικό', χρόνος=None, φωνή=None, διάλεκτος=None):
		αποτελέσματα = []
		if not λέξη:
			return αποτελέσματα
		
		κΛέξη = self.τ.κωδικοποιητής(λέξη)
		κΑποτελέσματα = self._κλίνε(κΛέξη, αριθμός, πτώση, γένος, χρόνος, φωνή, διάλεκτος)
		
		for κΑποτέλεσμα in κΑποτελέσματα:
			λέξη = self.τ.απο(κΑποτέλεσμα, True)
			if λέξη not in αποτελέσματα:
				αποτελέσματα.append(λέξη)
		
		return αποτελέσματα
			
if __name__ == "__main__":
	from δοκιμές.Μετοχῶν import Δοκιμές_Μετοχῶν
	δμ = Δοκιμές_Μετοχῶν()
	δμ.δοκιμές_αναγνώρισης()
	δμ.δοκιμές_κλίσης()

#"βιοὺς": {
#			"αρσενικό": [["βιοὺς"], ["βιόντος"], ["βιόντι"], ["βιόντα"], ["βιοὺς"], ["βιόντε"], ["βιόντοιν"], ["βιόντοιν"], ["βιόντε"], ["βιόντε"], ["βιόντες"], ["βιόντων"], ["βιοῦσι"], ["βιόντας"], ["βιόντες"]],
#			"θηλυκό"  : [["βιοῦσα"], ["βιούσης"], ["βιούσῃ"], ["βιοῦσαν"], ["βιοῦσα"], ["βιούσα"], ["βιούσαιν"], ["βιούσαιν"], ["βιούσα"], ["βιούσα"], ["βιοῦσαι"], ["βιουσῶν"], ["βιούσαις"], ["βιούσας"], ["βιοῦσαι"]],
#			"ουδέτερο": [["βιὸν"], ["βιόντος"], ["βιόντι"], ["βιὸν"], ["βιὸν"], ["βιόντε"], ["βιόντοιν"], ["βιόντοιν"], ["βιόντε"], ["βιόντε"], ["βιόντα"], ["βιόντων"], ["βιοῦσι"], ["βιόντα"], ["βιόντα"]]
#		},
#		"βὰς": {
#			"αρσενικό": [["βὰς"], ["βάντος"], ["βάντι"], ["βάντα"], ["βὰς"], ["βάντε"], ["βάντοιν"], ["βάντοιν"], ["βάντε"], ["βάντε"], ["βάντες"], ["βάντων"], ["βᾶσι"], ["βάντας"], ["βάντες"]],
#			"θηλυκό"  : [["βᾶσα"], ["βάσης"], ["βάσῃ"], ["βᾶσαν"], ["βᾶσα"], ["βάσα"], ["βάσαιν"], ["βάσαιν"], ["βάσα"], ["βάσα"], ["βᾶσαι"], ["βασῶν"], ["βάσαις"], ["βάσας"], ["βᾶσαι"]],
#			"ουδέτερο": [["βὰν"], ["βάντος"], ["βάντι"], ["βὰν"], ["βὰν"], ["βάντε"], ["βάντοιν"], ["βάντοιν"], ["βάντε"], ["βάντε"], ["βάντα"], ["βάντων"], ["βᾶσι"], ["βάντα"], ["βάντα"]]
#		},
#		"γεγονὼς": {
#			"αρσενικό": [["γεγονὼς"], ["γεγονότος"], ["γεγονότι"], ["γεγονότα"], ["γεγονὼς"], ["γεγονότε"], ["γεγονότοιν"], ["γεγονότοιν"], ["γεγονότε"], ["γεγονότε"], ["γεγονότες"], ["γεγονότων"], ["γεγονόσι"], ["γεγονότας"], ["γεγονότες"]],
#			"θηλυκό"  : [["γεγονυῖα"], ["γεγονυίας"], ["γεγονυίᾳ"], ["γεγονυῖαν"], ["γεγονυῖα"], ["γεγονυία"], ["γεγονυίαιν"], ["γεγονυίαιν"], ["γεγονυία"], ["γεγονυία"], ["γεγονυῖαι"], ["γεγονυιῶν"], ["γεγονυίαις"], ["γεγονυίας"], ["γεγονυῖαι"]],
#			"ουδέτερο": [["γεγονὸς"], ["γεγονότος"], ["γεγονότι"], ["γεγονὸς"], ["γεγονὸς"], ["γεγονότε"], ["γεγονότοιν"], ["γεγονότοιν"], ["γεγονότε"], ["γεγονότε"], ["γεγονότα"], ["γεγονότων"], ["γεγονόσι"], ["γεγονότα"], ["γεγονότα"]]
#		},
#		"γεγραφὼς": {
#			"αρσενικό": [["γεγραφὼς"], ["γεγραφότος"], ["γεγραφότι"], ["γεγραφότα"], ["γεγραφὼς"], ["γεγραφότε"], ["γεγραφότοιν"], ["γεγραφότοιν"], ["γεγραφότε"], ["γεγραφότε"], ["γεγραφότες"], ["γεγραφότων"], ["γεγραφόσι"], ["γεγραφότας"], ["γεγραφότες"]],
#			"θηλυκό"  : [["γεγραφυῖα"], ["γεγραφυίας"], ["γεγραφυίᾳ"], ["γεγραφυῖαν"], ["γεγραφυῖα"], ["γεγραφυία"], ["γεγραφυίαιν"], ["γεγραφυίαιν"], ["γεγραφυία"], ["γεγραφυία"], ["γεγραφυῖαι"], ["γεγραφυιῶν"], ["γεγραφυίαις"], ["γεγραφυίας"], ["γεγραφυῖαι"]],
#			"ουδέτερο": [["γεγραφὸς"], ["γεγραφότος"], ["γεγραφότι"], ["γεγραφὸς"], ["γεγραφὸς"], ["γεγραφότε"], ["γεγραφότοιν"], ["γεγραφότοιν"], ["γεγραφότε"], ["γεγραφότε"], ["γεγραφότα"], ["γεγραφότων"], ["γεγραφόσι"], ["γεγραφότα"], ["γεγραφότα"]]
#		},
#		"γνοὺς": {
#			"αρσενικό": [["γνοὺς"], ["γνόντος"], ["γνόντι"], ["γνόντα"], ["γνοὺς"], ["γνόντε"], ["γνόντοιν"], ["γνόντοιν"], ["γνόντε"], ["γνόντε"], ["γνόντες"], ["γνόντων"], ["γνοῦσι"], ["γνόντας"], ["γνόντες"]],
#			"θηλυκό"  : [["γνοῦσα"], ["γνούσης"], ["γνούσῃ"], ["γνοῦσαν"], ["γνοῦσα"], ["γνούσα"], ["γνούσαιν"], ["γνούσαιν"], ["γνούσα"], ["γνούσα"], ["γνοῦσαι"], ["γνουσῶν"], ["γνούσαις"], ["γνούσας"], ["γνοῦσαι"]],
#			"ουδέτερο": [["γνὸν"], ["γνόντος"], ["γνόντι"], ["γνὸν"], ["γνὸν"], ["γνόντε"], ["γνόντοιν"], ["γνόντοιν"], ["γνόντε"], ["γνόντε"], ["γνόντα"], ["γνόντων"], ["γνοῦσι"], ["γνόντα"], ["γνόντα"]]
#		},
#		"γράφων": {
#			"αρσενικό": [["γράφων"], ["γράφοντος"], ["γράφοντι"], ["γράφοντα"], ["γράφων"], ["γράφοντε"], ["γραφόντοιν"], ["γραφόντοιν"], ["γράφοντε"], ["γράφοντε"], ["γράφοντες"], ["γραφόντων"], ["γράφουσι"], ["γράφοντας"], ["γράφοντες"]],
#			"θηλυκό"  : [["γράφουσα"], ["γραφούσης"], ["γραφούσῃ"], ["γράφουσαν"], ["γράφουσα"], ["γραφούσα"], ["γραφούσαιν"], ["γραφούσαιν"], ["γραφούσα"], ["γραφούσα"], ["γράφουσαι"], ["γραφουσῶν"], ["γραφούσαις"], ["γραφούσας"], ["γράφουσαι"]],
#			"ουδέτερο": [["γράφον"], ["γράφοντος"], ["γράφοντι"], ["γράφον"], ["γράφον"], ["γράφοντε"], ["γραφόντοιν"], ["γραφόντοιν"], ["γράφοντε"], ["γράφοντε"], ["γράφοντα"], ["γραφόντων"], ["γράφουσι"], ["γράφοντα"], ["γράφοντα"]]
#		},
#		"γράψας": {
#			"αρσενικό": [["γράψας"], ["γράψαντος"], ["γράψαντι"], ["γράψαντα"], ["γράψας"], ["γράψαντε"], ["γράψαντοιν"], ["γράψαντοιν"], ["γράψαντε"], ["γράψαντε"], ["γράψαντες"], ["γραψάντων"], ["γράψασι"], ["γράψαντας"], ["γράψαντες"]],
#			"θηλυκό"  : [["γράψασα"], ["γράψασης"], ["γράψασῃ"], ["γράψασαν"], ["γράψασα"], ["γράψασα"], ["γράψασαιν"], ["γράψασαιν"], ["γράψασα"], ["γράψασα"], ["γράψασαι"], ["γραψάσων"], ["γράψασαις"], ["γράψασας"], ["γράψασαι"]],
#			"ουδέτερο": [["γράψαν"], ["γράψαντος"], ["γράψαντι"], ["γράψαν"], ["γράψαν"], ["γράψαντε"], ["γράψαντοιν"], ["γράψαντοιν"], ["γράψαντε"], ["γράψαντε"], ["γράψαντα"], ["γραψάντων"], ["γράψασι"], ["γράψαντα"], ["γράψαντα"]]
#		},
#		"γράψων": {
#			"αρσενικό": [["γράψων"], ["γράψοντος"], ["γράψοντι"], ["γράψοντα"], ["γράψων"], ["γράψοντε"], ["γραψόντοιν"], ["γραψόντοιν"], ["γράψοντε"], ["γράψοντε"], ["γράψοντες"], ["γραψόντων"], ["γράψουσι"], ["γράψοντας"], ["γράψοντες"]],
#			"θηλυκό"  : [["γράψουσα"], ["γραψούσης"], ["γραψούσῃ"], ["γράψουσαν"], ["γράψουσα"], ["γραψούσα"], ["γραψούσαιν"], ["γραψούσαιν"], ["γραψούσα"], ["γραψούσα"], ["γράψουσαι"], ["γραψουσῶν"], ["γραψούσαις"], ["γραψούσας"], ["γράψουσαι"]],
#			"ουδέτερο": [["γράψον"], ["γράψοντος"], ["γράψοντι"], ["γράψον"], ["γράψον"], ["γράψοντε"], ["γραψόντοιν"], ["γραψόντοιν"], ["γράψοντε"], ["γράψοντε"], ["γράψοντα"], ["γραψόντων"], ["γράψουσι"], ["γράψοντα"], ["γράψοντα"]]
#		},
#		"δεδιὼς": {
#			"αρσενικό": [["δεδιὼς"], ["δεδιότος"], ["δεδιότι"], ["δεδιότα"], ["δεδιὼς"], ["δεδιότε"], ["δεδιότοιν"], ["δεδιότοιν"], ["δεδιότε"], ["δεδιότε"], ["δεδιότες"], ["δεδιότων"], ["δεδιόσι"], ["δεδιότας"], ["δεδιότες"]],
#			"θηλυκό"  : [["δεδιυῖα"], ["δεδιυίας"], ["δεδιυίᾳ"], ["δεδιυῖαν"], ["δεδιυῖα"], ["δεδιυία"], ["δεδιυίαιν"], ["δεδιυίαιν"], ["δεδιυία"], ["δεδιυία"], ["δεδιυῖαι"], ["δεδιυιῶν"], ["δεδιυίαις"], ["δεδιυίας"], ["δεδιυῖαι"]],
#			"ουδέτερο": [["δεδιὸς"], ["δεδιότος"], ["δεδιότι"], ["δεδιὸς"], ["δεδιὸς"], ["δεδιότε"], ["δεδιότοιν"], ["δεδιότοιν"], ["δεδιότε"], ["δεδιότε"], ["δεδιότα"], ["δεδιότων"], ["δεδιόσι"], ["δεδιότα"], ["δεδιότα"]]
#		},
#		"δεδοικὼς": {
#			"αρσενικό": [["δεδοικὼς"], ["δεδοικότος"], ["δεδοικότι"], ["δεδοικότα"], ["δεδοικὼς"], ["δεδοικότε"], ["δεδοικότοιν"], ["δεδοικότοιν"], ["δεδοικότε"], ["δεδοικότε"], ["δεδοικότες"], ["δεδοικότων"], ["δεδοικόσι"], ["δεδοικότας"], ["δεδοικότες"]],
#			"θηλυκό"  : [["δεδοικυῖα"], ["δεδοικυίας"], ["δεδοικυίᾳ"], ["δεδοικυῖαν"], ["δεδοικυῖα"], ["δεδοικυία"], ["δεδοικυίαιν"], ["δεδοικυίαιν"], ["δεδοικυία"], ["δεδοικυία"], ["δεδοικυῖαι"], ["δεδοικυιῶν"], ["δεδοικυίαις"], ["δεδοικυίας"], ["δεδοικυῖαι"]],
#			"ουδέτερο": [["δεδοικὸς"], ["δεδοικότος"], ["δεδοικότι"], ["δεδοικὸς"], ["δεδοικὸς"], ["δεδοικότε"], ["δεδοικότοιν"], ["δεδοικότοιν"], ["δεδοικότε"], ["δεδοικότε"], ["δεδοικότα"], ["δεδοικότων"], ["δεδοικόσι"], ["δεδοικότα"], ["δεδοικότα"]]
#		},
#		"δὺς": {
#			"αρσενικό": [["δὺς"], ["δύντος"], ["δύντι"], ["δύντα"], ["δὺς"], ["δύντε"], ["δύντοιν"], ["δύντοιν"], ["δύντε"], ["δύντε"], ["δύντες"], ["δύντων"], ["δῦσι"], ["δύντας"], ["δύντες"]],
#			"θηλυκό"  : [["δῦσα"], ["δύσης"], ["δύσῃ"], ["δῦσαν"], ["δῦσα"], ["δύσα"], ["δύσαιν"], ["δύσαιν"], ["δύσα"], ["δύσα"], ["δῦσαι"], ["δυσῶν"], ["δύσαις"], ["δύσας"], ["δῦσαι"]],
#			"ουδέτερο": [["δὺν"], ["δύντος"], ["δύντι"], ["δὺν"], ["δὺν"], ["δύντε"], ["δύντοιν"], ["δύντοιν"], ["δύντε"], ["δύντε"], ["δύντα"], ["δύντων"], ["δῦσι"], ["δύντα"], ["δύντα"]]
#		},
#		"εἰδὼς": {
#			"αρσενικό": [["εἰδὼς"], ["εἰδότος"], ["εἰδότι"], ["εἰδότα"], ["εἰδὼς"], ["εἰδότε"], ["εἰδότοιν"], ["εἰδότοιν"], ["εἰδότε"], ["εἰδότε"], ["εἰδότες"], ["εἰδότων"], ["εἰδόσι"], ["εἰδότας"], ["εἰδότες"]],
#			"θηλυκό"  : [["εἰδυῖα"], ["εἰδυίας"], ["εἰδυίᾳ"], ["εἰδυῖαν"], ["εἰδυῖα"], ["εἰδυία"], ["εἰδυίαιν"], ["εἰδυίαιν"], ["εἰδυία"], ["εἰδυία"], ["εἰδυῖαι"], ["εἰδυιῶν"], ["εἰδυίαις"], ["εἰδυίας"], ["εἰδυῖαι"]],
#			"ουδέτερο": [["εἰδὸς"], ["εἰδότος"], ["εἰδότι"], ["εἰδὸς"], ["εἰδὸς"], ["εἰδότε"], ["εἰδότοιν"], ["εἰδότοιν"], ["εἰδότε"], ["εἰδότε"], ["εἰδότα"], ["εἰδότων"], ["εἰδόσι"], ["εἰδότα"], ["εἰδότα"]]
#		},
#		"εἰκὼς": {
#			"αρσενικό": [["εἰκὼς"], ["εἰκότος"], ["εἰκότι"], ["εἰκότα"], ["εἰκὼς"], ["εἰκότε"], ["εἰκότοιν"], ["εἰκότοιν"], ["εἰκότε"], ["εἰκότε"], ["εἰκότες"], ["εἰκότων"], ["εἰκόσι"], ["εἰκότας"], ["εἰκότες"]],
#			"θηλυκό"  : [["εἰκυῖα"], ["εἰκυίας"], ["εἰκυίᾳ"], ["εἰκυῖαν"], ["εἰκυῖα"], ["εἰκυία"], ["εἰκυίαιν"], ["εἰκυίαιν"], ["εἰκυία"], ["εἰκυία"], ["εἰκυῖαι"], ["εἰκυιῶν"], ["εἰκυίαις"], ["εἰκυίας"], ["εἰκυῖαι"]],
#			"ουδέτερο": [["εἰκὸς"], ["εἰκότος"], ["εἰκότι"], ["εἰκὸς"], ["εἰκὸς"], ["εἰκότε"], ["εἰκότοιν"], ["εἰκότοιν"], ["εἰκότε"], ["εἰκότε"], ["εἰκότα"], ["εἰκότων"], ["εἰκόσι"], ["εἰκότα"], ["εἰκότα"]]
#		},
#		"μείνας": {
#			"αρσενικό": [["μείνας"], ["μείναντος"], ["μείναντι"], ["μείναντα"], ["μείνας"], ["μείναντε"], ["μείναντοιν"], ["μείναντοιν"], ["μείναντε"], ["μείναντε"], ["μείναντες"], ["μεινάντων"], ["μείνασι"], ["μείναντας"], ["μείναντες"]],
#			"θηλυκό"  : [["μείνασα"], ["μείνασης"], ["μείνασῃ"], ["μείνασαν"], ["μείνασα"], ["μείνασα"], ["μείνασαιν"], ["μείνασαιν"], ["μείνασα"], ["μείνασα"], ["μείνασαι"], ["μεινάσων"], ["μείνασαις"], ["μείνασας"], ["μείνασαι"]],
#			"ουδέτερο": [["μεῖναν"], ["μείναντος"], ["μείναντι"], ["μεῖναν"], ["μεῖναν"], ["μείναντε"], ["μείναντοιν"], ["μείναντοιν"], ["μείναντε"], ["μείναντε"], ["μείναντα"], ["μεινάντων"], ["μείνασι"], ["μείναντα"], ["μείναντα"]]
#		},
#		"μενῶν": {
#			"αρσενικό": [["μενῶν"], ["μενοῦντος"], ["μενοῦντι"], ["μενοῦντα"], ["μενῶν"], ["μενοῦντε"], ["μενούντοιν"], ["μενούντοιν"], ["μενοῦντε"], ["μενοῦντε"], ["μενοῦντες"], ["μενούντων"], ["μενοῦσι"], ["μενοῦντας"], ["μενοῦντες"]],
#			"θηλυκό"  : [["μενοῦσα"], ["μενούσης"], ["μενούσῃ"], ["μενοῦσαν"], ["μενοῦσα"], ["μενούσα"], ["μενούσαιν"], ["μενούσαιν"], ["μενούσα"], ["μενούσα"], ["μενοῦσαι"], ["μενουσῶν"], ["μενούσαις"], ["μενούσας"], ["μενοῦσαι"]],
#			"ουδέτερο": [["μενοῦν"], ["μενοῦντος"], ["μενοῦντι"], ["μενοῦν"], ["μενοῦν"], ["μενοῦντε"], ["μενούντοιν"], ["μενούντοιν"], ["μενοῦντε"], ["μενοῦντε"], ["μενοῦντα"], ["μενούντων"], ["μενοῦσι"], ["μενοῦντα"], ["μενοῦντα"]]
#		},
#		"πληγεὶς": {
#			"αρσενικό": [["πληγεὶς"], ["πληγέντος"], ["πληγέντι"], ["πληγέντα"], ["πληγεὶς"], ["πληγέντε"], ["πληγέντοιν"], ["πληγέντοιν"], ["πληγέντε"], ["πληγέντε"], ["πληγέντες"], ["πληγέντων"], ["πληγεῖσι"], ["πληγέντας"], ["πληγέντες"]],
#			"θηλυκό"  : [["πληγεῖσα"], ["πληγείσης"], ["πληγείσῃ"], ["πληγεῖσαν"], ["πληγεῖσα"], ["πληγείσα"], ["πληγείσαιν"], ["πληγείσαιν"], ["πληγείσα"], ["πληγείσα"], ["πληγεῖσαι"], ["πληγεισῶν"], ["πληγείσαις"], ["πληγείσας"], ["πληγεῖσαι"]],
#			"ουδέτερο": [["πληγὲν"], ["πληγέντος"], ["πληγέντι"], ["πληγὲν"], ["πληγὲν"], ["πληγέντε"], ["πληγέντοιν"], ["πληγέντοιν"], ["πληγέντε"], ["πληγέντε"], ["πληγέντα"], ["πληγέντων"], ["πληγεῖσι"], ["πληγέντα"], ["πληγέντα"]]
#		},
#		"ποιούμενος": {
#			"αρσενικό": [["ποιούμενος"], ["ποιουμένου"], ["ποιουμένῳ"], ["ποιούμενον"], ["ποιούμενε"], ["ποιουμένω"], ["ποιουμένοιν"], ["ποιουμένοιν"], ["ποιουμένω"], ["ποιουμένω"], ["ποιούμενοι"], ["ποιουμένων"], ["ποιουμένοις"], ["ποιουμένους"], ["ποιούμενοι"]],
#			"θηλυκό"  : [["ποιουμένη"], ["ποιουμένης"], ["ποιουμένῃ"], ["ποιουμένην"], ["ποιουμένη"], ["ποιούμενα"], ["ποιουμέναιν"], ["ποιουμέναιν"], ["ποιούμενα"], ["ποιούμενα"], ["ποιούμεναι"], ["ποιουμένων"], ["ποιουμέναις"], ["ποιουμένας"], ["ποιούμεναι"]],
#			"ουδέτερο": [["ποιούμενον"], ["ποιουμένου"], ["ποιουμένῳ"], ["ποιούμενον"], ["ποιούμενον"], ["ποιουμένω"], ["ποιουμένοιν"], ["ποιουμένοιν"], ["ποιουμένω"], ["ποιουμένω"], ["ποιούμενα"], ["ποιουμένων"], ["ποιουμένοις"], ["ποιούμενα"], ["ποιούμενα"]]
#		},
#		"ποιῶν": {
#			"αρσενικό": [["ποιῶν"], ["ποιοῦντος"], ["ποιοῦντι"], ["ποιοῦντα"], ["ποιῶν"], ["ποιοῦντε"], ["ποιούντοιν"], ["ποιούντοιν"], ["ποιοῦντε"], ["ποιοῦντε"], ["ποιοῦντες"], ["ποιούντων"], ["ποιοῦσι"], ["ποιοῦντας"], ["ποιοῦντες"]],
#			"θηλυκό"  : [["ποιοῦσα"], ["ποιούσης"], ["ποιούσῃ"], ["ποιοῦσαν"], ["ποιοῦσα"], ["ποιούσα"], ["ποιούσαιν"], ["ποιούσαιν"], ["ποιούσα"], ["ποιούσα"], ["ποιοῦσαι"], ["ποιουσῶν"], ["ποιούσαις"], ["ποιούσας"], ["ποιοῦσαι"]],
#			"ουδέτερο": [["ποιοῦν"], ["ποιοῦντος"], ["ποιοῦντι"], ["ποιοῦν"], ["ποιοῦν"], ["ποιοῦντε"], ["ποιούντοιν"], ["ποιούντοιν"], ["ποιοῦντε"], ["ποιοῦντε"], ["ποιοῦντα"], ["ποιούντων"], ["ποιοῦσι"], ["ποιοῦντα"], ["ποιοῦντα"]]
#		},
#		"τεθνεὼς": {
#			"αρσενικό": [["τεθνεὼς"], ["τεθνεῶτος"], ["τεθνεῶτι"], ["τεθνεῶτα"], ["τεθνεὼς"], ["τεθνεῶτε"], ["τεθνεώτοιν"], ["τεθνεώτοιν"], ["τεθνεῶτε"], ["τεθνεῶτε"], ["τεθνεῶτες"], ["τεθνεώτων"], ["τεθνεῶσι"], ["τεθνεῶτας"], ["τεθνεῶτες"]],
#			"θηλυκό"  : [["τεθνεῶσα"], ["τεθνεώσης"], ["τεθνεώσῃ"], ["τεθνεῶσαν"], ["τεθνεῶσα"], ["τεθνεώσα"], ["τεθνεώσαιν"], ["τεθνεώσαιν"], ["τεθνεώσα"], ["τεθνεώσα"], ["τεθνεῶσαι"], ["τεθνεωσῶν"], ["τεθνεώσαις"], ["τεθνεῶσας"], ["τεθνεῶσαι"]],
#			"ουδέτερο": [["τεθνεὼς"], ["τεθνεῶτος"], ["τεθνεῶτι"], ["τεθνεὼς"], ["τεθνεὼς"], ["τεθνεῶτε"], ["τεθνεώτοιν"], ["τεθνεώτοιν"], ["τεθνεῶτε"], ["τεθνεῶτε"], ["τεθνεῶτα"], ["τεθνεώτων"], ["τεθνεῶσι"], ["τεθνεῶτα"], ["τεθνεῶτα"]]
#		},
#		"τεθνηκὼς": {
#			"αρσενικό": [["τεθνηκὼς"], ["τεθνηκότος"], ["τεθνηκότι"], ["τεθνηκότα"], ["τεθνηκὼς"], ["τεθνηκότε"], ["τεθνηκότοιν"], ["τεθνηκότοιν"], ["τεθνηκότε"], ["τεθνηκότε"], ["τεθνηκότες"], ["τεθνηκότων"], ["τεθνηκόσι"], ["τεθνηκότας"], ["τεθνηκότες"]],
#			"θηλυκό"  : [["τεθνηκυῖα"], ["τεθνηκυίας"], ["τεθνηκυίᾳ"], ["τεθνηκυῖαν"], ["τεθνηκυῖα"], ["τεθνηκυία"], ["τεθνηκυίαιν"], ["τεθνηκυίαιν"], ["τεθνηκυία"], ["τεθνηκυία"], ["τεθνηκυῖαι"], ["τεθνηκυιῶν"], ["τεθνηκυίαις"], ["τεθνηκυίας"], ["τεθνηκυῖαι"]],
#			"ουδέτερο": [["τεθνηκὸς"], ["τεθνηκότος"], ["τεθνηκότι"], ["τεθνηκὸς"], ["τεθνηκὸς"], ["τεθνηκότε"], ["τεθνηκότοιν"], ["τεθνηκότοιν"], ["τεθνηκότε"], ["τεθνηκότε"], ["τεθνηκότα"], ["τεθνηκότων"], ["τεθνηκόσι"], ["τεθνηκότα"], ["τεθνηκότα"]]
#		},
#		"φοιτῶν": {
#			"αρσενικό": [["φοιτῶν"], ["φοιτῶντος"], ["φοιτῶντι"], ["φοιτῶντα"], ["φοιτῶν"], ["φοιτῶντε"], ["φοιτώντοιν"], ["φοιτώντοιν"], ["φοιτῶντε"], ["φοιτῶντε"], ["φοιτῶντες"], ["φοιτώντων"], ["φοιτῶσι"], ["φοιτῶντας"], ["φοιτῶντες"]],
#			"θηλυκό"  : [["φοιτῶσα"], ["φοιτώσης"], ["φοιτώσῃ"], ["φοιτῶσαν"], ["φοιτῶσα"], ["φοιτώσα"], ["φοιτώσαιν"], ["φοιτώσαιν"], ["φοιτώσα"], ["φοιτώσα"], ["φοιτῶσαι"], ["φοιτωσῶν"], ["φοιτώσαις"], ["φοιτώσας"], ["φοιτῶσαι"]],
#			"ουδέτερο": [["φοιτῶν"], ["φοιτῶντος"], ["φοιτῶντι"], ["φοιτῶν"], ["φοιτῶν"], ["φοιτῶντε"], ["φοιτώντοιν"], ["φοιτώντοιν"], ["φοιτῶντε"], ["φοιτῶντε"], ["φοιτῶντα"], ["φοιτώντων"], ["φοιτῶσι"], ["φοιτῶντα"], ["φοιτῶντα"]]
#		},
#		"φυγών": {
#			"αρσενικό": [["φυγών"], ["φυγόντος"], ["φυγόντι"], ["φυγόντα"], ["φυγών"], ["φυγόντε"], ["φυγόντοιν"], ["φυγόντοιν"], ["φυγόντε"], ["φυγόντε"], ["φυγόντες"], ["φυγόντων"], ["φυγοῦσι"], ["φυγόντας"], ["φυγόντες"]],
#			"θηλυκό"  : [["φυγοῦσα"], ["φυγούσης"], ["φυγούσῃ"], ["φυγοῦσαν"], ["φυγοῦσα"], ["φυγούσα"], ["φυγούσαιν"], ["φυγούσαιν"], ["φυγούσα"], ["φυγούσα"], ["φυγοῦσαι"], ["φυγουσῶν"], ["φυγούσαις"], ["φυγούσας"], ["φυγοῦσαι"]],
#			"ουδέτερο": [["φυγὸν"], ["φυγόντος"], ["φυγόντι"], ["φυγὸν"], ["φυγὸν"], ["φυγόντε"], ["φυγόντοιν"], ["φυγόντοιν"], ["φυγόντε"], ["φυγόντε"], ["φυγόντα"], ["φυγόντων"], ["φυγοῦσι"], ["φυγόντα"], ["φυγόντα"]]
#		},
#		"φὺς": {
#			"αρσενικό": [["φὺς"], ["φύντος"], ["φύντι"], ["φύντα"], ["φὺς"], ["φύντε"], ["φύντοιν"], ["φύντοιν"], ["φύντε"], ["φύντε"], ["φύντες"], ["φύντων"], ["φῦσι"], ["φύντας"], ["φύντες"]],
#			"θηλυκό"  : [["φῦσα"], ["φύσης"], ["φύσῃ"], ["φῦσαν"], ["φῦσα"], ["φύσα"], ["φύσαιν"], ["φύσαιν"], ["φύσα"], ["φύσα"], ["φῦσαι"], ["φυσῶν"], ["φύσαις"], ["φύσας"], ["φῦσαι"]],
#			"ουδέτερο": [["φὺν"], ["φύντος"], ["φύντι"], ["φὺν"], ["φὺν"], ["φύντε"], ["φύντοιν"], ["φύντοιν"], ["φύντε"], ["φύντε"], ["φύντα"], ["φύντων"], ["φῦσι"], ["φύντα"], ["φύντα"]]
#		},
#		"ἀποδρὰς": {
#			"αρσενικό": [["ἀποδρὰς"], ["ἀποδράντος"], ["ἀποδράντι"], ["ἀποδράντα"], ["ἀποδρὰς"], ["ἀποδράντε"], ["ἀποδράντοιν"], ["ἀποδράντοιν"], ["ἀποδράντε"], ["ἀποδράντε"], ["ἀποδράντες"], ["ἀποδράντων"], ["ἀποδρᾶσι"], ["ἀποδράντας"], ["ἀποδράντες"]],
#			"θηλυκό"  : [["ἀποδρᾶσα"], ["ἀποδράσης"], ["ἀποδράσῃ"], ["ἀποδρᾶσαν"], ["ἀποδρᾶσα"], ["ἀποδράσα"], ["ἀποδράσαιν"], ["ἀποδράσαιν"], ["ἀποδράσα"], ["ἀποδράσα"], ["ἀποδρᾶσαι"], ["ἀποδρασῶν"], ["ἀποδράσαις"], ["ἀποδράσας"], ["ἀποδρᾶσαι"]],
#			"ουδέτερο": [["ἀποδρὰν"], ["ἀποδράντος"], ["ἀποδράντι"], ["ἀποδρὰν"], ["ἀποδρὰν"], ["ἀποδράντε"], ["ἀποδράντοιν"], ["ἀποδράντοιν"], ["ἀποδράντε"], ["ἀποδράντε"], ["ἀποδράντα"], ["ἀποδράντων"], ["ἀποδρᾶσι"], ["ἀποδράντα"], ["ἀποδράντα"]]
#		},
#		"ἀπολλὺς": {
#			"αρσενικό": [["ἀπολλὺς"], ["ἀπολλύντος"], ["ἀπολλύντι"], ["ἀπολλύντα"], ["ἀπολλὺς"], ["ἀπολλύντε"], ["ἀπολλύντοιν"], ["ἀπολλύντοιν"], ["ἀπολλύντε"], ["ἀπολλύντε"], ["ἀπολλύντες"], ["ἀπολλύντων"], ["ἀπολλῦσι"], ["ἀπολλύντας"], ["ἀπολλύντες"]],
#			"θηλυκό"  : [["ἀπολλῦσα"], ["ἀπολλύσης"], ["ἀπολλύσῃ"], ["ἀπολλῦσαν"], ["ἀπολλῦσα"], ["ἀπολλύσα"], ["ἀπολλύσαιν"], ["ἀπολλύσαιν"], ["ἀπολλύσα"], ["ἀπολλύσα"], ["ἀπολλῦσαι"], ["ἀπολλυσῶν"], ["ἀπολλύσαις"], ["ἀπολλύσας"], ["ἀπολλῦσαι"]],
#			"ουδέτερο": [["ἀπολλὺν"], ["ἀπολλύντος"], ["ἀπολλύντι"], ["ἀπολλὺν"], ["ἀπολλὺν"], ["ἀπολλύντε"], ["ἀπολλύντοιν"], ["ἀπολλύντοιν"], ["ἀπολλύντε"], ["ἀπολλύντε"], ["ἀπολλύντα"], ["ἀπολλύντων"], ["ἀπολλῦσι"], ["ἀπολλύντα"], ["ἀπολλύντα"]]
#		},
#		"ἁλοὺς": {
#			"αρσενικό": [["ἁλοὺς"], ["ἁλόντος"], ["ἁλόντι"], ["ἁλόντα"], ["ἁλοὺς"], ["ἁλόντε"], ["ἁλόντοιν"], ["ἁλόντοιν"], ["ἁλόντε"], ["ἁλόντε"], ["ἁλόντες"], ["ἁλόντων"], ["ἁλοῦσι"], ["ἁλόντας"], ["ἁλόντες"]],
#			"θηλυκό"  : [["ἁλοῦσα"], ["ἁλούσης"], ["ἁλούσῃ"], ["ἁλοῦσαν"], ["ἁλοῦσα"], ["ἁλούσα"], ["ἁλούσαιν"], ["ἁλούσαιν"], ["ἁλούσα"], ["ἁλούσα"], ["ἁλοῦσαι"], ["ἁλουσῶν"], ["ἁλούσαις"], ["ἁλούσας"], ["ἁλοῦσαι"]],
#			"ουδέτερο": [["ἁλὸν"], ["ἁλόντος"], ["ἁλόντι"], ["ἁλὸν"], ["ἁλὸν"], ["ἁλόντε"], ["ἁλόντοιν"], ["ἁλόντοιν"], ["ἁλόντε"], ["ἁλόντε"], ["ἁλόντα"], ["ἁλόντων"], ["ἁλοῦσι"], ["ἁλόντα"], ["ἁλόντα"]]
#		},
#		"ἐλευθερῶν": {
#			"αρσενικό": [["ἐλευθερῶν"], ["ἐλευθεροῦντος"], ["ἐλευθεροῦντι"], ["ἐλευθεροῦντα"], ["ἐλευθερῶν"], ["ἐλευθεροῦντε"], ["ἐλευθερούντοιν"], ["ἐλευθερούντοιν"], ["ἐλευθεροῦντε"], ["ἐλευθεροῦντε"], ["ἐλευθεροῦντες"], ["ἐλευθερούντων"], ["ἐλευθεροῦσι"], ["ἐλευθεροῦντας"], ["ἐλευθεροῦντες"]],
#			"θηλυκό"  : [["ἐλευθεροῦσα"], ["ἐλευθερούσης"], ["ἐλευθερούσῃ"], ["ἐλευθεροῦσαν"], ["ἐλευθεροῦσα"], ["ἐλευθερούσα"], ["ἐλευθερούσαιν"], ["ἐλευθερούσαιν"], ["ἐλευθερούσα"], ["ἐλευθερούσα"], ["ἐλευθεροῦσαι"], ["ἐλευθερουσῶν"], ["ἐλευθερούσαις"], ["ἐλευθερούσας"], ["ἐλευθεροῦσαι"]],
#			"ουδέτερο": [["ἐλευθεροῦν"], ["ἐλευθεροῦντος"], ["ἐλευθεροῦντι"], ["ἐλευθεροῦν"], ["ἐλευθεροῦν"], ["ἐλευθεροῦντε"], ["ἐλευθερούντοιν"], ["ἐλευθερούντοιν"], ["ἐλευθεροῦντε"], ["ἐλευθεροῦντε"], ["ἐλευθεροῦντα"], ["ἐλευθερούντων"], ["ἐλευθεροῦσι"], ["ἐλευθεροῦντα"], ["ἐλευθεροῦντα"]]
#		},
#		"ἐλῶν": {
#			"αρσενικό": [["ἐλῶν"], ["ἐλῶντος"], ["ἐλῶντι"], ["ἐλῶντα"], ["ἐλῶν"], ["ἐλῶντε"], ["ἐλώντοιν"], ["ἐλώντοιν"], ["ἐλῶντε"], ["ἐλῶντε"], ["ἐλῶντες"], ["ἐλώντων"], ["ἐλῶσι"], ["ἐλῶντας"], ["ἐλῶντες"]],
#			"θηλυκό"  : [["ἐλῶσα"], ["ἐλώσης"], ["ἐλώσῃ"], ["ἐλῶσαν"], ["ἐλῶσα"], ["ἐλώσα"], ["ἐλώσαιν"], ["ἐλώσαιν"], ["ἐλώσα"], ["ἐλώσα"], ["ἐλῶσαι"], ["ἐλωσῶν"], ["ἐλώσαις"], ["ἐλώσας"], ["ἐλῶσαι"]],
#			"ουδέτερο": [["ἐλῶν"], ["ἐλῶντος"], ["ἐλῶντι"], ["ἐλῶν"], ["ἐλῶν"], ["ἐλῶντε"], ["ἐλώντοιν"], ["ἐλώντοιν"], ["ἐλῶντε"], ["ἐλῶντε"], ["ἐλῶντα"], ["ἐλώντων"], ["ἐλῶσι"], ["ἐλῶντα"], ["ἐλῶντα"]]
#		},
#		"ἐμπιπλὰς": {
#			"αρσενικό": [["ἐμπιπλὰς"], ["ἐμπιπλάντος"], ["ἐμπιπλάντι"], ["ἐμπιπλάντα"], ["ἐμπιπλὰς"], ["ἐμπιπλάντε"], ["ἐμπιπλάντοιν"], ["ἐμπιπλάντοιν"], ["ἐμπιπλάντε"], ["ἐμπιπλάντε"], ["ἐμπιπλάντες"], ["ἐμπιπλάντων"], ["ἐμπιπλᾶσι"], ["ἐμπιπλάντας"], ["ἐμπιπλάντες"]],
#			"θηλυκό"  : [["ἐμπιπλᾶσα"], ["ἐμπιπλάσης"], ["ἐμπιπλάσῃ"], ["ἐμπιπλᾶσαν"], ["ἐμπιπλᾶσα"], ["ἐμπιπλάσα"], ["ἐμπιπλάσαιν"], ["ἐμπιπλάσαιν"], ["ἐμπιπλάσα"], ["ἐμπιπλάσα"], ["ἐμπιπλᾶσαι"], ["ἐμπιπλασῶν"], ["ἐμπιπλάσαις"], ["ἐμπιπλάσας"], ["ἐμπιπλᾶσαι"]],
#			"ουδέτερο": [["ἐμπιπλὰν"], ["ἐμπιπλάντος"], ["ἐμπιπλάντι"], ["ἐμπιπλὰν"], ["ἐμπιπλὰν"], ["ἐμπιπλάντε"], ["ἐμπιπλάντοιν"], ["ἐμπιπλάντοιν"], ["ἐμπιπλάντε"], ["ἐμπιπλάντε"], ["ἐμπιπλάντα"], ["ἐμπιπλάντων"], ["ἐμπιπλᾶσι"], ["ἐμπιπλάντα"], ["ἐμπιπλάντα"]]
#		},
#		"ἑλών": {
#			"αρσενικό": [["ἑλών"], ["ἑλόντος"], ["ἑλόντι"], ["ἑλόντα"], ["ἑλών"], ["ἑλόντε"], ["ἑλόντοιν"], ["ἑλόντοιν"], ["ἑλόντε"], ["ἑλόντε"], ["ἑλόντες"], ["ἑλόντων"], ["ἑλοῦσι"], ["ἑλόντας"], ["ἑλόντες"]],
#			"θηλυκό"  : [["ἑλοῦσα"], ["ἑλούσης"], ["ἑλούσῃ"], ["ἑλοῦσαν"], ["ἑλοῦσα"], ["ἑλούσα"], ["ἑλούσαιν"], ["ἑλούσαιν"], ["ἑλούσα"], ["ἑλούσα"], ["ἑλοῦσαι"], ["ἑλουσῶν"], ["ἑλούσαις"], ["ἑλούσας"], ["ἑλοῦσαι"]],
#			"ουδέτερο": [["ἑλὸν"], ["ἑλόντος"], ["ἑλόντι"], ["ἑλὸν"], ["ἑλὸν"], ["ἑλόντε"], ["ἑλόντοιν"], ["ἑλόντοιν"], ["ἑλόντε"], ["ἑλόντε"], ["ἑλόντα"], ["ἑλόντων"], ["ἑλοῦσι"], ["ἑλόντα"], ["ἑλόντα"]]
#		},
#		"ἑστὼς": {
#			"αρσενικό": [["ἑστὼς"], ["ἑστῶτος"], ["ἑστῶτι"], ["ἑστῶτα"], ["ἑστὼς"], ["ἑστῶτε"], ["ἑστώτοιν"], ["ἑστώτοιν"], ["ἑστῶτε"], ["ἑστῶτε"], ["ἑστῶτες"], ["ἑστώτων"], ["ἑστῶσι"], ["ἑστῶτας"], ["ἑστῶτες"]],
#			"θηλυκό"  : [["ἑστῶσα"], ["ἑστώσης"], ["ἑστώσῃ"], ["ἑστῶσαν"], ["ἑστῶσα"], ["ἑστώσα"], ["ἑστώσαιν"], ["ἑστώσαιν"], ["ἑστώσα"], ["ἑστώσα"], ["ἑστῶσαι"], ["ἑστωσῶν"], ["ἑστώσαις"], ["ἑστῶσας"], ["ἑστῶσαι"]],
#			"ουδέτερο": [["ἑστὼς"], ["ἑστῶτος"], ["ἑστῶτι"], ["ἑστὼς"], ["ἑστὼς"], ["ἑστῶτε"], ["ἑστώτοιν"], ["ἑστώτοιν"], ["ἑστῶτε"], ["ἑστῶτε"], ["ἑστῶτα"], ["ἑστώτων"], ["ἑστῶσι"], ["ἑστῶτα"], ["ἑστῶτα"]]
#		},
#		"ἰδών": {
#			"αρσενικό": [["ἰδών"], ["ἰδόντος"], ["ἰδόντι"], ["ἰδόντα"], ["ἰδών"], ["ἰδόντε"], ["ἰδόντοιν"], ["ἰδόντοιν"], ["ἰδόντε"], ["ἰδόντε"], ["ἰδόντες"], ["ἰδόντων"], ["ἰδοῦσι"], ["ἰδόντας"], ["ἰδόντες"]],
#			"θηλυκό"  : [["ἰδοῦσα"], ["ἰδούσης"], ["ἰδούσῃ"], ["ἰδοῦσαν"], ["ἰδοῦσα"], ["ἰδούσα"], ["ἰδούσαιν"], ["ἰδούσαιν"], ["ἰδούσα"], ["ἰδούσα"], ["ἰδοῦσαι"], ["ἰδουσῶν"], ["ἰδούσαις"], ["ἰδούσας"], ["ἰδοῦσαι"]],
#			"ουδέτερο": [["ἰδόν", "ἰδὸν"], ["ἰδόντος"], ["ἰδόντι"], ["ἰδόν", "ἰδὸν"], ["ἰδόν", "ἰδὸν"], ["ἰδόντε"], ["ἰδόντοιν"], ["ἰδόντοιν"], ["ἰδόντε"], ["ἰδόντε"], ["ἰδόντα"], ["ἰδόντων"], ["ἰδοῦσι"], ["ἰδόντα"], ["ἰδόντα"]]
#		},
#		"ὤν": {
#			"αρσενικό": [["ὤν"], ["ὄντος"], ["ὄντι"], ["ὄντα"], ["ὤν"], ["ὄντε"], ["ὄντοιν"], ["ὄντοιν"], ["ὄντε"], ["ὄντε"], ["ὄντες"], ["ὄντων"], ["οὖσι"], ["ὄντας"], ["ὄντες"]],
#			"θηλυκό"  : [["οὖσα"], ["οὔσης"], ["οὔσῃ"], ["οὖσαν"], ["οὖσα"], ["οὔσα"], ["οὔσαιν"], ["οὔσαιν"], ["οὔσα"], ["οὔσα"], ["οὖσαι"], ["οὐσῶν"], ["οὔσαις"], ["οὔσας"], ["οὖσαι"]],
#			"ουδέτερο": [["ὂν", "ὄν"], ["ὄντος"], ["ὄντι"], ["ὂν", "ὄν"], ["ὂν", "ὄν"], ["ὄντε"], ["ὄντοιν"], ["ὄντοιν"], ["ὄντε"], ["ὄντε"], ["ὄντα"], ["ὄντων"], ["οὖσι"], ["ὄντα"], ["ὄντα"]]
#		},
#		"ῥυεὶς": {
#			"αρσενικό": [["ῥυεὶς"], ["ῥυέντος"], ["ῥυέντι"], ["ῥυέντα"], ["ῥυεὶς"], ["ῥυέντε"], ["ῥυέντοιν"], ["ῥυέντοιν"], ["ῥυέντε"], ["ῥυέντε"], ["ῥυέντες"], ["ῥυέντων"], ["ῥυεῖσι"], ["ῥυέντας"], ["ῥυέντες"]],
#			"θηλυκό"  : [["ῥυεῖσα"], ["ῥυείσης"], ["ῥυείσῃ"], ["ῥυεῖσαν"], ["ῥυεῖσα"], ["ῥυείσα"], ["ῥυείσαιν"], ["ῥυείσαιν"], ["ῥυείσα"], ["ῥυείσα"], ["ῥυεῖσαι"], ["ῥυεισῶν"], ["ῥυείσαις"], ["ῥυείσας"], ["ῥυεῖσαι"]],
#			"ουδέτερο": [["ῥυὲν"], ["ῥυέντος"], ["ῥυέντι"], ["ῥυὲν"], ["ῥυὲν"], ["ῥυέντε"], ["ῥυέντοιν"], ["ῥυέντοιν"], ["ῥυέντε"], ["ῥυέντε"], ["ῥυέντα"], ["ῥυέντων"], ["ῥυεῖσι"], ["ῥυέντα"], ["ῥυέντα"]]
#		}
