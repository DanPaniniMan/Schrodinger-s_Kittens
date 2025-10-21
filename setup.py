from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token="iwSNNOoSKI_JwE329HRmv5SxwGEj46VVScZxvr1qrmDI", overwrite=True)
service = QiskitRuntimeService()
service.backends()