#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012, dimitriadis dimitris
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#	 * Redistributions of source code must retain the above copyright
#		notice, this list of conditions and the following disclaimer.
#	 * Redistributions in binary form must reproduce the above copyright
#		notice, this list of conditions and the following disclaimer in the
#		documentation and/or other materials provided with the distribution.
#	 * Neither the name of the dimitriadis dimitris nor the
#		names of its contributors may be used to endorse or promote products
#		derived from this software without specific prior written permission.
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

import time

τύπωσε = print
κείμενο = str
μήκος = len
εύρος = range

class Θέματα():
	def __init__(self, sql, τονιστής):
		self.sql = sql
		self.τ = τονιστής
		
	def νέα(self, αναγνώριση, θέματα, μεταδεδομένα, κλίμακες, ομάδες, διάλεκτοι):
		διάλεκτος = αναγνώριση["διάλεκτος"]
		ΑΑ = αναγνώριση.get("ΑΑ")
		cur = self.sql.conn.cursor()
		σετ = {}
		if ΑΑ:
			for σύνολο in cur.execute(
				'select Κλειδί, Ἐτικέτες from Λήμματα where ΑΑ=? and Διάλεκτος=?;', 
					(ΑΑ, διάλεκτος)):
				if σύνολο:
						σετ[σύνολο[0]] = σύνολο[1]
			for k,v in σετ.items():
				if "τρέχον" in v:
					cur.execute('update Λήμματα set Ἐτικέτες=? where Κλειδί=?;', (v.replace("τρέχον", "ανενεργό"), k))
		else:
			αναγνώριση["ΑΑ"] = 1
			cur.execute('select max(ΑΑ) from Λήμματα where Διάλεκτος=?;', 
						(διάλεκτος, ))
			for c in cur:
				if c and c[0]:
					αναγνώριση["ΑΑ"] = c[0]+1
			
		self.__αποθήκευση(αναγνώριση)
		self.sql.conn.commit()
		self.φόρτωση(θέματα, μεταδεδομένα, κλίμακες, ομάδες, διάλεκτοι)
	
	def διαγραφή(self, αναγνώριση):
		cur = self.sql.conn.cursor()
		Κλειδί = αναγνώριση["Κλειδί"]
		σετ = []
		for σύνολο in cur.execute('select Ἐτικέτες from Λήμματα where Κλειδί=?;', (Κλειδί, )):
			if σύνολο:
				σετ.append(σύνολο[0])
		for σ in σετ:
			up = False
			if "διαγραμμένο" in σ:
				up = False
			elif "τρέχον" in σ:
				σ=σ.replace("τρέχον", "διαγραμμένο")
				up = True
			elif "ανενεργό" in σ:
				σ=σ.replace("ανενεργό", "διαγραμμένο")
				up = True
			if up:
				cur.execute('update Λήμματα set Ἐτικέτες=? where Κλειδί=?;', (σ, Κλειδί))
		self.sql.conn.commit()
	
	def τρέχον(self, αναγνώριση):
		ΑΑ = αναγνώριση["ΑΑ"]
		Κλειδί = αναγνώριση["Κλειδί"]
		διάλεκτος = αναγνώριση["διάλεκτος"]
		
		σετ = []
		τρέχον = None
		cur = self.sql.conn.cursor()
		for σύνολο in cur.execute(
			'select Κλειδί, Ἐτικέτες from Λήμματα where ΑΑ=? and Διάλεκτος=?;', 
			(ΑΑ, διάλεκτος)):
			if σύνολο and σύνολο[0]!=Κλειδί:
				σετ.append([σύνολο[0], σύνολο[1]])
			elif σύνολο[0]==Κλειδί:
				τρέχον = σύνολο[1]
		for σ in σετ:
			if "τρέχον" in σ[1]:
				cur.execute('update Λήμματα set Ἐτικέτες=? where Κλειδί=?;', (σ[1].replace("τρέχον", "ανενεργό"), σ[0]))
		if τρέχον:
			if "ανενεργό" in τρέχον:
				τρέχον = τρέχον.replace("ανενεργό", "")
			if "διαγραμμένο" in τρέχον:
				τρέχον = τρέχον.replace("διαγραμμένο", "")
			νέο_τρέχον = []
			for σ in τρέχον.split(","):
				σσ = σ.strip()
				if σσ:
					νέο_τρέχον.append(σσ)
			νέο_τρέχον.append("τρέχον")
			cur.execute('update Λήμματα set Ἐτικέτες=? where Κλειδί=?;', 
							(", ".join(νέο_τρέχον), Κλειδί))
		self.sql.conn.commit()
		
	def __αποθήκευση(self, σύνολο):
		# Προαιρετικά
		Ἡμερομηνία = σύνολο.get("Ἡμερομηνία")
		if not Ἡμερομηνία:
			Ἡμερομηνία = time.strftime("%Y%m%d%H%M%S")
		Συγγραφέας = σύνολο.get("Συγγραφέας")
		if not Συγγραφέας:
			Συγγραφέας = "admin"
		Ἐτικέτες = σύνολο.get("ἐτικέτες")
		if not Ἐτικέτες:
			Ἐτικέτες = "τρέχον, "
		Παρατηρήσεις = σύνολο.get("Παρατηρήσεις")
		if not Παρατηρήσεις:
			Παρατηρήσεις = ""
			
		# Υποχρεωτικά
		ΑΑ = σύνολο["ΑΑ"]
		Διάλεκτος = σύνολο["διάλεκτος"]
		Μεταδεδομένα = str(σύνολο["Μεταδεδομένα"])
		Κλίμακες = str(σύνολο["Κλίμακες"])
		συνθετικό = σύνολο["συνθετικό"]
		
		ενεστωτική_αύξηση = σύνολο["ενεστωτική αύξηση"]
		αύξηση = σύνολο["αύξηση"]
		αύξηση_παρακείμενου = σύνολο["αύξηση παρακείμενου"]
		Λήμμα = σύνολο["θέμα"]
		Ρήμα = σύνολο["ρήμα"]
		Μετοχή = σύνολο["μετοχή"]
		συχνότητα = σύνολο["συχνότητα"]
		
		cur = self.sql.conn.cursor()
		cur.execute('insert into Λήμματα (ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, '+
				'Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, "ενεστωτική αύξηση", '+
				'αύξηση, "αύξηση παρακείμενου", Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις) '+
				'values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
			(ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, 
			Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, ενεστωτική_αύξηση,
			αύξηση, αύξηση_παρακείμενου, Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις))
			
	def φόρτωση(self, θέματα, μεταδεδομένα, κλίμακες, ομάδες, διάλεκτοι, όλα=False):
		cur = self.sql.conn.cursor()
		if όλα:
			σύνολα = cur.execute('select Κλειδί, ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, ' + 
				'Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, "ενεστωτική αύξηση", '+
				'αύξηση, "αύξηση παρακείμενου", '+
				'Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις from Λήμματα as p ' + 
				'WHERE Ἡμερομηνία=(SELECT MAX(Ἡμερομηνία) FROM ' + 
				'Λήμματα WHERE ΑΑ=p.ΑΑ and Διάλεκτος=p.Διάλεκτος);')
		else:
			σύνολα = cur.execute('select Κλειδί, ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, ' + 
				'Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, "ενεστωτική αύξηση", '+
				'αύξηση, "αύξηση παρακείμενου", '+
				'Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις from Λήμματα as p ' + 
				'WHERE Ἡμερομηνία=(SELECT MAX(Ἡμερομηνία) FROM Λήμματα ' + 
				'WHERE ΑΑ=p.ΑΑ and Διάλεκτος=p.Διάλεκτος AND Ἐτικέτες LIKE "%τρέχον%");')
		self.sql.conn.commit()
		for σύνολο in σύνολα:
			Κλειδί, ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, ενεστωτική_αύξηση, αύξηση, αύξηση_παρακείμενου, Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις = σύνολο
			
			θέμα = {}
			Διάλεκτος0 = Διάλεκτος
			if διάλεκτοι[Διάλεκτος]['εικονική']:
				Διάλεκτος0 = διάλεκτοι[Διάλεκτος]['εικονική']
			if Ρήμα>0 and not ομάδες["ρήμα"][Διάλεκτος0][Ρήμα]:
				print("Ρήμα:"+Λήμμα+" λείπει η ομάδα", Ρήμα, "στην διάλεκτο",Διάλεκτος, Διάλεκτος0)
			elif όλα:
				θέμα["ρήμα"] = Ρήμα
			else:
				θέμα["ρήμα"] = ομάδες["ρήμα"][Διάλεκτος0][Ρήμα]
			
			if Μετοχή>0 and not ομάδες["μετοχή"][Διάλεκτος0][Μετοχή]:
				print("Μετοχή:"+Λήμμα+" λείπει η ομάδα", Μετοχή, "στην διάλεκτο",Διάλεκτος, Διάλεκτος0)
			elif όλα:
				θέμα["μετοχή"] = Μετοχή
			else:
				θέμα["μετοχή"] = ομάδες["μετοχή"][Διάλεκτος0][Μετοχή]
			
			θέμα["Κλειδί"] = Κλειδί
			θέμα["ΑΑ"] = ΑΑ
			θέμα["διάλεκτος"] = Διάλεκτος
			θέμα["Ἡμερομηνία"] = Ἡμερομηνία
			θέμα["Συγγραφέας"] = Συγγραφέας
			θέμα["ἐτικέτες"] = Ἐτικέτες
			θέμα["μέρος του λόγου"] = "ρήμα"
			
			θέμα["Μεταδεδομένα"] = {}
			for απόκλιση in eval(Μεταδεδομένα):
				μ = μεταδεδομένα[Διάλεκτος][απόκλιση]
				if μ:
					θέμα["Μεταδεδομένα"][μ["ὄνομα"]] = μ["τιμές"]
			
			θέμα["Κλίμακες"] = {}			
			for απόκλιση in eval(Κλίμακες):
				κ = κλίμακες[Διάλεκτος][απόκλιση]
				if κ:
					θέμα["Κλίμακες"][κ["ὄνομα"]] = κ["τιμή"]
			θέμα["συνθετικό"] = συνθετικό
			θέμα["λήμμα"] = Λήμμα
			if όλα:
				pass
#				if Διάλεκτος not in κατηγοριοτονισμoί:
#					κατηγοριοτονισμoί[Διάλεκτος] = {}
#				if κατηγορία not in κατηγοριοτονισμoί[Διάλεκτος]:
#					κατηγοριοτονισμoί[Διάλεκτος][κατηγορία] = []
#				if τονισμός not in κατηγοριοτονισμoί[Διάλεκτος][κατηγορία]:
#					κατηγοριοτονισμoί[Διάλεκτος][κατηγορία].append(τονισμός)
#					κατηγοριοτονισμoί[Διάλεκτος][κατηγορία].sort()
			else:
				θέμα["κΛέξη"] = self.τ.κωδικοποιητής(Λήμμα)
				if συνθετικό:
					θέμα["κΣυνθετικό"] = self.τ.κωδικοποιητής(συνθετικό)
				if αύξηση:
					θέμα["κΑύξηση"] = self.τ.κωδικοποιητής(αύξηση)
				if ενεστωτική_αύξηση:
					θέμα["κΕνεστωτική αύξηση"] = self.τ.κωδικοποιητής(ενεστωτική_αύξηση)
				if αύξηση_παρακείμενου:
					θέμα["κΑύξηση παρακείμενου"] = self.τ.κωδικοποιητής(αύξηση_παρακείμενου)
					
			θέμα["αύξηση"] = αύξηση
			θέμα["ενεστωτική αύξηση"] = ενεστωτική_αύξηση
			θέμα["αύξηση παρακείμενου"] = αύξηση_παρακείμενου
			θέμα["συχνότητα"] = συχνότητα
			θέμα["Παρατηρήσεις"] = Παρατηρήσεις
			
			θέματα.append(θέμα)
	
	def ιστορικό(self, αναγνώριση, μεταδεδομένα, κλίμακες, ομάδες):
		αποτέλεσμα = []
		ΑΑ = αναγνώριση["ΑΑ"]
		if ΑΑ!=None:
			cur = self.sql.conn.cursor()
			σύνολα = cur.execute('select Κλειδί, ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, ' + 
				'Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, "ενεστωτική αύξηση", '+
				'αύξηση, "αύξηση παρακείμενου", '+
				'Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις from Λήμματα as p ' + 
				'WHERE ΑΑ=? and Διάλεκτος=?;', 
				(ΑΑ, αναγνώριση["διάλεκτος"]))
			for σύνολο in σύνολα:
				Κλειδί, ΑΑ, Διάλεκτος, Ἡμερομηνία, Συγγραφέας, Ἐτικέτες, Μεταδεδομένα, Κλίμακες, συνθετικό, ενεστωτική_αύξηση, αύξηση, αύξηση_παρακείμενου, Λήμμα, Ρήμα, Μετοχή, συχνότητα, Παρατηρήσεις = σύνολο
				
				θέμα = {}
				if Ρήμα>0 and not ομάδες["ρήμα"][Διάλεκτος][Ρήμα]:
					print("Ρήμα:"+Λήμμα+" λείπει η ομάδα", Ρήμα, "στην διάλεκτο",Διάλεκτος)
				else:
					θέμα["ρήμα"] = Ρήμα
				
				if Μετοχή>0 and not ομάδες["μετοχή"][Διάλεκτος][Μετοχή]:
					print("Μετοχή:"+Λήμμα+" λείπει η ομάδα", Μετοχή, "στην διάλεκτο",Διάλεκτος)
				else:
					θέμα["μετοχή"] = Μετοχή
				
				θέμα["Κλειδί"] = Κλειδί
				θέμα["ΑΑ"] = ΑΑ
				θέμα["διάλεκτος"] = Διάλεκτος
				θέμα["Ἡμερομηνία"] = Ἡμερομηνία
				θέμα["Συγγραφέας"] = Συγγραφέας
				θέμα["ἐτικέτες"] = Ἐτικέτες
				θέμα["μέρος του λόγου"] = "ρήμα"
				
				θέμα["Μεταδεδομένα"] = {}
				for απόκλιση in eval(Μεταδεδομένα):
					μ = μεταδεδομένα[Διάλεκτος][απόκλιση]
					if μ:
						θέμα["Μεταδεδομένα"][μ["ὄνομα"]] = μ["τιμές"]
				
				θέμα["Κλίμακες"] = {}			
				for απόκλιση in eval(Κλίμακες):
					κ = κλίμακες[Διάλεκτος][απόκλιση]
					if κ:
						θέμα["Κλίμακες"][κ["ὄνομα"]] = κ["τιμή"]
				θέμα["συνθετικό"] = συνθετικό
				θέμα["λήμμα"] = Λήμμα
				θέμα["αύξηση"] = αύξηση
				θέμα["ενεστωτική αύξηση"] = ενεστωτική_αύξηση
				θέμα["αύξηση παρακείμενου"] = αύξηση_παρακείμενου
				θέμα["συχνότητα"] = συχνότητα
				θέμα["Παρατηρήσεις"] = Παρατηρήσεις
				
				αποτέλεσμα.append(θέμα)
			self.sql.conn.commit()
		return αποτέλεσμα
		
	def αποθήκευση(self, πίνακας, δεδομένα):
		cur = self.conn.cursor()
		cur.execute('select * from "'+πίνακας+'";')
		cur.execute('delete from "'+πίνακας+'";')
		self.conn.commit()
		Ημερομηνία = time.strftime("%Y%m%d%H%M%S")
		μτλ = None
		if "Τονισμοί" in πίνακας:
			pass
		elif "Ανώμαλ" in πίνακας:
			pass
		elif "Καταλήξεις" in πίνακας:
			pass
		elif πίνακας in ["Λήμματα", "Επίθετα", "Μετοχές", "Ρήματα", "Λήμματα"]:
			if πίνακας in ["Μετοχές", "Ρήματα", "Λήμματα"]:
				for πιν in ["χρόνοι", "Ρήματα", "μετοχῶν", "Μετοχές", "Λήμματα"]:
					cur.execute('select * from "'+πιν+'";')
					cur.execute('delete from "'+πιν+'";')
				self.conn.commit()
			for Διάλεκτος, σύνολα in δεδομένα.items():
				ΑΑ = 0
				for σύνολο in σύνολα:
					self.αποθήκευση_λέξης(σύνολο, ΑΑ, Ημερομηνία)
					ΑΑ += 1
			self.conn.commit()
			