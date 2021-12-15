# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbiAKCmZyb20gQ1NWIGltcG9ydCBDU1YKZnJvbSBKU09OIGltcG9ydCBKU09OCmZyb20gTkZUIGltcG9ydCBORlQKCgpyb290ID0gVGsoKQoKcm9vdC5nZW9tZXRyeSgnNzUweDc1MCcpCnJvb3QucmVzaXphYmxlKEZhbHNlLCBGYWxzZSkKcm9vdC50aXRsZSgiTkZUcyBVcGxvYWQgdG8gT3BlblNlYSB2MS4wIikKICAKaW5wdXRfc2F2ZV9saXN0ID0gWyJORlRzIGZvbGRlciA6IiwgMCwgMCwgMCwgMCwgMCwgMCwgMCwgMF0KbWFpbl9kaXJlY3RvcnkgPSBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0pCgoKZGVmIHN1cHBvcnRVUkwoKToKICAgIHdlYmJyb3dzZXIub3Blbl9uZXcoImh0dHBzOi8vd3d3LmluZm90cmV4Lm5ldC9vcGVuc2VhL3N1cHBvcnQuYXNwP3I9YXBwIikKCgpjbGFzcyBXZWJJbWFnZToKICAgIGRlZiBfX2luaXRfXyhzZWxmLCB1cmwpOgogICAgICAgIHdpdGggdXJsbGliLnJlcXVlc3QudXJsb3Blbih1cmwpIGFzIHU6CiAgICAgICAgICAgIHJhd19kYXRhID0gdS5yZWFkKCkKICAgICAgICAjc2VsZi5pbWFnZSA9IHRrLlBob3RvSW1hZ2UoZGF0YT1iYXNlNjQuZW5jb2RlYnl0ZXMocmF3X2RhdGEpKQogICAgICAgIGltYWdlID0gSW1hZ2Uub3Blbihpby5CeXRlc0lPKHJhd19kYXRhKSkKICAgICAgICBzZWxmLmltYWdlID0gSW1hZ2VUay5QaG90b0ltYWdlKGltYWdlKQoKICAgIGRlZiBnZXQoc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYuaW1hZ2UKaW1hZ2V1cmwgPSAiaHR0cHM6Ly93d3cuaW5mb3RyZXgubmV0L29wZW5zZWEvaGVhZGVyLnBuZyIKaW1nID0gV2ViSW1hZ2UoaW1hZ2V1cmwpLmdldCgpCmltYWdlbGFiID0gdGsuTGFiZWwocm9vdCwgaW1hZ2U9aW1nKQppbWFnZWxhYi5ncmlkKHJvdz0wLCBjb2x1bW5zcGFuPTIpCmltYWdlbGFiLmJpbmQoIjxCdXR0b24tMT4iLCBsYW1iZGEgZTpzdXBwb3J0VVJMKCkpCgppc19wb2x5Z29uID0gQm9vbGVhblZhcigpCmlzX3BvbHlnb24uc2V0KEZhbHNlKSAKCmRlZiBvcGVuX2Nocm9tZV9wcm9maWxlKCk6CiAgICBzdWJwcm9jZXNzLlBvcGVuKAogICAgICAgIFsKICAgICAgICAgICAgInN0YXJ0IiwKICAgICAgICAgICAgImNocm9tZSIsCiAgICAgICAgICAgICItLXJlbW90ZS1kZWJ1Z2dpbmctcG9ydD04OTg5IiwKICAgICAgICAgICAgIi0tdXNlci1kYXRhLWRpcj0iICsgbWFpbl9kaXJlY3RvcnkgKyAiL2Nocm9tZV9wcm9maWxlIiwKICAgICAgICBdLAogICAgICAgIHNoZWxsPVRydWUsCiAgICApCgoKZGVmIHNhdmVfZmlsZV9wYXRoKCk6CiAgICAjcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZmlsZS5jbG91ZCIpIAogICAgcmV0dXJuIG9zLnBhdGguam9pbihzeXMucGF0aFswXSwgIlNhdmVfZ3VpLmNsb3VkIikgCgoKIyBhc2sgZm9yIGRpcmVjdG9yeSBvbiBjbGlja2luZyBidXR0b24sIGNoYW5nZXMgYnV0dG9uIG5hbWUuCmRlZiB1cGxvYWRfZm9sZGVyX2lucHV0KCk6CiAgICBnbG9iYWwgdXBsb2FkX3BhdGgKICAgIHVwbG9hZF9wYXRoID0gZmlsZWRpYWxvZy5hc2tkaXJlY3RvcnkoKQogICAgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX3BhdGgpCgpkZWYgTmFtZV9jaGFuZ2VfaW1nX2ZvbGRlcl9idXR0b24odXBsb2FkX2ZvbGRlcl9pbnB1dCk6CiAgICB1cGxvYWRfZm9sZGVyX2lucHV0X2J1dHRvblsidGV4dCJdID0gdXBsb2FkX2ZvbGRlcl9pbnB1dAoKZGVmIGlzX251bWVyaWModmFsKToKCWlmIHN0cih2YWwpLmlzZGlnaXQoKToKCQlyZXR1cm4gVHJ1ZQoJZWxpZiBzdHIodmFsKS5yZXBsYWNlKCcuJywnJywxKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsc2U6CgkJcmV0dXJuIEZhbHNlCgpjbGFzcyBJbnB1dEZpZWxkOgogICAgZGVmIF9faW5pdF9fKHNlbGYsIGxhYmVsLCByb3dfaW8sIGNvbHVtbl9pbywgcG9zLCAgbWFzdGVyPXJvb3QpOgogICAgICAgIHNlbGYubWFzdGVyID0gbWFzdGVyCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZCA9IEVudHJ5KHNlbGYubWFzdGVyLCB3aWR0aD02MCkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmdyaWQoaXBhZHk9MykKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsID0gTGFiZWwobWFzdGVyLCB0ZXh0PWxhYmVsLCBhbmNob3I9InciLCB3aWR0aD0yMCwgaGVpZ2h0PTEgKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQubGFiZWwuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKHJvdz1yb3dfaW8sIGNvbHVtbj1jb2x1bW5faW8gKyAxLCBwYWR4PTEyLCBwYWR5PTIpCiAgICAgICAgdHJ5OgogICAgICAgICAgICB3aXRoIG9wZW4oc2F2ZV9maWxlX3BhdGgoKSwgInJiIikgYXMgaW5maWxlOgogICAgICAgICAgICAgICAgbmV3X2RpY3QgPSBwaWNrbGUubG9hZChpbmZpbGUpCiAgICAgICAgICAgICAgICBzZWxmLmluc2VydF90ZXh0KG5ld19kaWN0W3Bvc10pCiAgICAgICAgZXhjZXB0IEZpbGVOb3RGb3VuZEVycm9yOgogICAgICAgICAgICBwYXNzCiAgICAgICAgCiAgICBkZWYgaW5zZXJ0X3RleHQoc2VsZiwgdGV4dCk6CiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5kZWxldGUoMCwgImVuZCIpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5pbnNlcnQoMCwgdGV4dCkKCiAgICBkZWYgc2F2ZV9pbnB1dHMoc2VsZiwgcG9zKToKICAgICAgICAjbWVzc2FnZWJveC5zaG93d2FybmluZygic2hvd3dhcm5pbmciLCAiV2FybmluZyIpCiAgICAgICAgaW5wdXRfc2F2ZV9saXN0Lmluc2VydChwb3MsIHNlbGYuaW5wdXRfZmllbGQuZ2V0KCkpCiAgICAgICAgd2l0aCBvcGVuKHNhdmVfZmlsZV9wYXRoKCksICJ3YiIpIGFzIG91dGZpbGU6CiAgICAgICAgICAgIHBpY2tsZS5kdW1wKGlucHV0X3NhdmVfbGlzdCwgb3V0ZmlsZSkKICAgICAgICAgICAgCiAgICBkZWYgdmFsaWRhdGVfaW5wdXR'
love = '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'
god = 'AgICAgKQogICAgICAgIAogICAgZGVmIHdhaXRfY3NzX3NlbGVjdG9yVGVzdChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKAogICAgICAgICAgICBFeHBlY3RlZENvbmRpdGlvbnMuZWxlbWVudFRvQmVDbGlja2FibGUoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKSAgICAKCiAgICBkZWYgd2FpdF94cGF0aChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoKEJ5LlhQQVRILCBjb2RlKSkpCgoKICAgIHdoaWxlIGVuZF9udW0gPj0gc3RhcnRfbnVtOgogICAgICAgIHByaW50KCJTdGFydCBjcmVhdGluZyBORlQgIiArICBsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpCiAgICAgICAgcHJpbnQoJ251bWJlciAnLCAgc3RhcnRfbnVtKQogICAgICAgIGRyaXZlci5nZXQoY29sbGVjdGlvbl9saW5rKQoKICAgICAgICB3YWl0X3hwYXRoKCcvLypbQGlkPSJtZWRpYSJdJykKICAgICAgICBpbWFnZVVwbG9hZCA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Im1lZGlhIl0nKQogICAgICAgIGltYWdlUGF0aCA9IG9zLnBhdGguYWJzcGF0aChmaWxlX3BhdGggKyAiXFxpbWFnZXNcXCIgKyBzdHIoc3RhcnRfbnVtKSArICIuIiArIGxvb3BfZmlsZV9mb3JtYXQpICAjIGNoYW5nZSBmb2xkZXIgaGVyZQogICAgICAgIGltYWdlVXBsb2FkLnNlbmRfa2V5cyhpbWFnZVBhdGgpCiAgICAgICAgdGltZS5zbGVlcCgyKQoKICAgICAgICBuYW1lID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibmFtZSJdJykKICAgICAgICBuYW1lLnNlbmRfa2V5cyhsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpICAjICsxMDAwIGZvciBvdGhlciBmb2xkZXJzICNjaGFuZ2UgbmFtZSBiZWZvcmUgIiMiCiAgICAgICAgdGltZS5zbGVlcCgxLjUpCgogICAgICAgIGV4dF9saW5rID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iZXh0ZXJuYWxfbGluayJdJykKICAgICAgICBleHRfbGluay5zZW5kX2tleXMobG9vcF9leHRlcm5hbF9saW5rKQogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgZGVzYyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9ImRlc2NyaXB0aW9uIl0nKQogICAgICAgIGRlc2Muc2VuZF9rZXlzKGxvb3BfZGVzY3JpcHRpb24pCiAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAjanNvbkRhdGEgPSBKU09OKGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCgogICAgICAgIGpzb25GaWxlID0gZmlsZV9wYXRoICsgIi9qc29uLyIrIHN0cihzdGFydF9udW0pICsgIi5qc29uIgogICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKGpzb25GaWxlKSBhbmQgb3MuYWNjZXNzKGpzb25GaWxlLCBvcy5SX09LKToKICAgICAgICAgICAKICAgICAgICAgICAgI3ByaW50KHN0cihqc29uTWV0YURhdGEpKQogICAgICAgICAgICB3YWl0X2Nzc19zZWxlY3RvcigiYnV0dG9uW2FyaWEtbGFiZWw9J0FkZCBwcm9wZXJ0aWVzJ10iKQogICAgICAgICAgICBwcm9wZXJ0aWVzID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgZHJpdmVyLmV4ZWN1dGVfc2NyaXB0KCJhcmd1bWVudHNbMF0uY2xpY2soKTsiLCBwcm9wZXJ0aWVzKQogICAgICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgICAgICAjIGpzb25EYXRhID0gSlNPTihvcy5nZXRjd2QoKSArICIvZGF0YS8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIpLnJlYWRGcm9tRmlsZSgpCiAgICAgICAgICAgICMganNvbk1ldGFEYXRhID0ganNvbkRhdGFbJ2F0dHJpYnV0ZXMnXQoKICAgICAgICAgICAgICMgY2hlY2tzIGlmIGZpbGUgZXhpc3RzCiAgICAgICAgICAgIGpzb25EYXRhID0ganNvbi5sb2FkcyhvcGVuKGZpbGVfcGF0aCArICJcXCIgICsgIlxcanNvblxcIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkKCkpCiAgICAgICAgICAgIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgIGZvciBrZXkgaW4ganNvbk1ldGFEYXRhOgogICAgICAgICAgICAgICAgaW5wdXQxID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy90Ym9keVtAY2xhc3M9IkFzc2V0VHJhaXRzRm9ybS0tYm9keSJdL3RyW2xhc3QoKV0vdGRbMV0vZGl2L2Rpdi9pbnB1dCcpCiAgICAgICAgICAgICAgICBpbnB1dDIgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL3Rib2R5W0BjbGFzcz0iQXNzZXRUcmFpdHNGb3JtLS1ib2R5Il0vdHJbbGFzdCgpXS90ZFsyXS9kaXYvZGl2L2lucHV0JykKICAgICAgICAgICAgICAgICNwcmludChzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgI3ByaW50KHN0cihrZXlbJ3ZhbHVlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQxLnNlbmRfa2V5cyhzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQyLnNlbmRfa2V5cyhzdHIoa2V5Wyd2YWx1ZSddKSkKICAgICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vYnV0dG9uW3RleHQoKT0iQWRkIG1vcmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgwLjgpCgogICAgICAgICAgICBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL2J1dHRvblt0ZXh0KCk9IlNhdmUiXScpLmNsaWNrKCkKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAjIFNlbGVjdCBQb2x5Z29uIGJsb2NrY2hhaW4gaWYgYXBwbGljYWJsZQogICAgICAgIGlmIGlzX3BvbHlnb24uZ2V0KCk6CiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgJy8vKltAaWQ9Il9fbmV4dCJdL2RpdlsxXS9tYWluL2Rpdi9kaXYvc2VjdGlvbi9kaXYvZm9ybS9kaXZbN10vZGl2L2RpdlsyXScpCiAgICAgICAgICAgIGJsb2NrY2hhaW5fYnV0dG9uLmNsaWNrKCkKICAgICAgICAgICAgcG9seWdvbl9idXR0b25fbG9jYXRpb24gPSAnLy9zcGFuW25vcm1hbGl6ZS1zcGFjZSgpID0gIk11bWJhaSJdJwogICAgICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoCiAgICAgICAgICAgICAgICAoQnkuWFBBVEgsIHBvbHlnb25fYnV0dG9uX2xvY2F0aW9uKSkpCiAgICAgICAgICAgIHBvbHlnb25fYnV0dG9uID0gZHJpdmVyLmZpbmRfZWxlbWVudCgKICAgICAgICAgICAgICAgIEJ5LlhQQVRILCBwb2x5Z29uX2J1dHRvbl9sb2NhdGlvbikKICAgICAgICAgICAgcG9seWdvbl9idXR0b24uY2xpY2soKQoKCiAgICAgICAgY3JlYXRlID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0iX19uZXh0Il0vZGl2WzFdL21haW4vZGl2L2Rpdi9zZWN0aW9uL2RpdlsyXS9mb3JtL2Rpdi9kaXZbMV0vc3Bhbi9idXR0b24nKQogICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgY3JlYXRlK'
destiny = 'DbtVPNtVPNtVUEcoJHhp2kyMKNbZFxXPvNtVPNtVPNtq2ScqS9wp3Asp2IfMJA0o3VbVzyoLKWcLF1fLJWyoQ0aD2kip2HaKFVcPvNtVPNtVPNtL3Wip3ZtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvnIgupzyuYJkuLzIfCFqQoT9mMFqqVvxXVPNtVPNtVPOwpz9mpl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPOgLJyhK3OuM2HtCFOxpzy2MKVhL3IlpzIhqS93nJ5xo3qsnTShMTkyPvNtVPNtVPNtq2ScqS94pTS0nPtaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9xnKMoZI0iMTy2Y3AjLJ5oZy0iLFpcPvNtVPNtVPNtp2IfoPN9VTElnKMypv5znJ5xK2IfMJ1yoaEsLaysrUOuqTtbWl8iXygNnJD9Vy9sozI4qPWqY2EcqyfkKF9gLJyhY2Ecqv9xnKLiMTy2JmSqY2Ecqv9mpTShJmWqY2RaXDbtVPNtVPNtVUAyoTjhL2kcL2fbXDbXPvNtVPNtVPNtq2ScqS9wp3Asp2IfMJA0o3VbVzyhpUI0J3OfLJAynT9fMTIlCFqOoJ91oaDaKFVcPvNtVPNtVPNtLJ1iqJ50VQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI9wp3Asp2IfMJA0o3VbVzyhpUI0J3OfLJAynT9fMTIlCFqOoJ91oaDaKFVcPvNtVPNtVPNtLJ1iqJ50YaAyozEsn2I5plumqUVboT9ipS9jpzywMFxcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvLaI0qT9hJ3E5pTH9W3A1Lz1cqPqqVvxXVPNtVPNtVPOfnKA0nJ5aVQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI9wp3Asp2IfMJA0o3VbVzW1qUEioyg0rKOyCFqmqJWgnKDaKFVcPvNtVPNtVPNtoTymqTyhMl5woTywnltcPvNtVPNtVPNtqTygMF5moTIypPt1XDbXVPNtVPNtVPNwMz9lVRkcqzHXVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvLaI0qT9hJ2AfLKAmCFqPo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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))