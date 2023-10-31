# 3 components of my solution
## I used Linode/Akamai instead of Digital Ocean

In the assignment a VPS was proposed to be set up in Digital Ocean but I had already an account on Linode/Akamai. So I choose to provison a VPS on that platform.
It made it a little less comfortable as I couldn't quite trust that the assignment was one on one applicable, but it appeared to be no problem at all.

The VPS is the virtual hardware that the code is sent to and where the publishing/compiling takes place that is needed to be able to see the outcome as a website with a browser like Chrome or Safari.

## GitHub Actions

I have split the Actions in two sections: a Test section and a dependable Build section. In the Test section I test wether the code is written properly with a linter and then I test it with a test writen in pytest. 
To be honest I have inplemented a almost faketest as I have put a function that adds two numbers with no use at all in the code that I test, because that was the easiest for this assignment. In real life it wouldn't make any sense. 

It took me a long while and a lot of trial and error to find out what works and what not and what piece of test should be done where, and also where it is executed, before it is build. 

## SSH as authentication

The hardest part (for me) was the SSH implementation. The whole shebang about public and private keys on one machine and the other can be mixed up pretty easily and before you know it, you end up with an tangled piece of information spaghetti. 
I found out that it takes a cool head to untangle the puzzle and I did. 

# Conclussion

This assignment wasn't the hardest in theory. 

In real life and in practice is appeared to be a tough cookie, becasue of all the little possible mismatches on either plarform and component. It takes a brave set of brains to keep the clear path out of the fuzzy haze. 
