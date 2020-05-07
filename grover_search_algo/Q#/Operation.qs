namespace Microsoft.Quantum.Tutorial.Grover{
    open Microsoft.Quantum.Intrinsic; //https://docs.microsoft.com/en-us/qsharp/api/qsharp/microsoft.quantum.intrinsic
    open Microsoft.Quantum.Canon; // CZ
    open Microsoft.Quantum.Arrays; // for each

    operation Search(nQubits : Int) : Result[]{
        using (qubits = Qubit[nQubits]){
            ApplyToEach(H, qubits);
            ApplyToEach(X, qubits);
            Controlled Z([qubits[0]], qubits[1]);
            // Oracle for |00⟩ :
            ApplyToEach(X, qubits);
            ApplyToEach(H, qubits);
            ApplyToEach(Z, qubits);
            Controlled Z([qubits[0]], qubits[1]);
            ApplyToEach(H, qubits);
            return ForEach(M, qubits);
        }
    }
}