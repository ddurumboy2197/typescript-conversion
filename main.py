Men sizga TypeScript ni qo'shish uchun JavaScript faylini yozaman. 

```typescript
// User.js
export interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

// UserRepository.js
export interface UserRepository {
  createUser(user: User): Promise<User>;
  getUser(id: number): Promise<User | null>;
  updateUser(id: number, user: User): Promise<User>;
  deleteUser(id: number): Promise<void>;
}

// UserService.js
export class UserService {
  private userRepository: UserRepository;

  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository;
  }

  public async createUser(user: User): Promise<User> {
    return this.userRepository.createUser(user);
  }

  public async getUser(id: number): Promise<User | null> {
    return this.userRepository.getUser(id);
  }

  public async updateUser(id: number, user: User): Promise<User> {
    return this.userRepository.updateUser(id, user);
  }

  public async deleteUser(id: number): Promise<void> {
    return this.userRepository.deleteUser(id);
  }
}

// App.js
import { UserService } from './UserService';
import { UserRepository } from './UserRepository';

class InMemoryUserRepository implements UserRepository {
  private users: User[] = [];

  public async createUser(user: User): Promise<User> {
    this.users.push(user);
    return user;
  }

  public async getUser(id: number): Promise<User | null> {
    return this.users.find((user) => user.id === id) || null;
  }

  public async updateUser(id: number, user: User): Promise<User> {
    const existingUser = this.users.find((u) => u.id === id);
    if (existingUser) {
      Object.assign(existingUser, user);
      return existingUser;
    }
    return null;
  }

  public async deleteUser(id: number): Promise<void> {
    this.users = this.users.filter((user) => user.id !== id);
  }
}

const userRepository = new InMemoryUserRepository();
const userService = new UserService(userRepository);

const user: User = {
  id: 1,
  name: 'John Doe',
  email: 'john.doe@example.com',
  password: 'password',
};

userService.createUser(user).then((createdUser) => {
  console.log(createdUser);
});

userService.getUser(1).then((user) => {
  console.log(user);
});

userService.updateUser(1, {
  name: 'Jane Doe',
  email: 'jane.doe@example.com',
  password: 'newpassword',
}).then((updatedUser) => {
  console.log(updatedUser);
});

userService.deleteUser(1).then(() => {
  console.log('User deleted');
});
```
