#!/bin/bash
kubectl get pod | grep jupyter-test-2duser- | cut -d' '  -f1 | xargs kubectl delete pod
kubectl get pvc | grep claim-test-2duser- | cut -d' ' -f1 | xargs kubectl delete pvc
